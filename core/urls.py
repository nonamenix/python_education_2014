from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import create_api_user, create_user


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='core/about.html')),
    url(r'^developer/create', create_api_user),
    url(r'^user/create', create_user),
)
