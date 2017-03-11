from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings        # FOR STATIC AND MEDIA FILE ACCESS

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^', include('nodarb.urls')),

]

