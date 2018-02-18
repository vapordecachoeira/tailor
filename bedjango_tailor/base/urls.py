from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.views.i18n import JavaScriptCatalog

from . import views


def home(request):
    return redirect('/admin')


urlpatterns = [
    url(r'^', include('users.urls')),
    url(r'^$', home, name='index'),
    url(r'^admin/', include(admin.site.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
