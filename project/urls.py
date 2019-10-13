from django.views.generic import TemplateView
from django.conf.urls import include, url

from django.contrib import admin

from simple_robots.views import serve_robots


api_url_patterns = [
    url(r'^auth/', include('rest_auth.urls')),

    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^auth/accounts/', include('allauth.urls')),

]


urlpatterns = [
    url(r'^api/', include(api_url_patterns)),
    url(r'^robots.txt$', serve_robots),
    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^admin/', admin.site.urls),

]
