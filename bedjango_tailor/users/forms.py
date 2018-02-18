from django.contrib.auth.forms import ReadOnlyPasswordHashField

from base.validators import is_password_secure
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.validators import validate_email, RegexValidator
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm

from .models import User


class UserRegisterForm(RegistrationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        validators=[RegexValidator(
                        regex=is_password_secure,
                        code=_('Invalid password'))],
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        validators=[RegexValidator(
                        regex=is_password_secure,
                        code=_('Invalid password'))],
        )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'date_joined', 'slug', 'country', 'email', 'preferred_language')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(label=_("Email"), required=True,
                            widget=forms.TextInput(attrs={'placeholder': _('Your email')}))
    password = forms.CharField(label=_("Password"), max_length=32,
                               widget=forms.PasswordInput(attrs={'placeholder': _('Your password')}),
                               required=True, validators=[
                                    RegexValidator(
                                        regex=is_password_secure,
                                        code=_('Invalid password'))],)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        return email

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            try:
                username = get_user_model().objects.get(email=email).username
            except:
                raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
        return self.cleaned_data
