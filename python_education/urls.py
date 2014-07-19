from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(get_redirect_url=lambda: '/api/')),
    url(r'^api/', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
