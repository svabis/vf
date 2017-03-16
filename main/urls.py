from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings	# FOR STATIC AND MEDIA FILE ACCESS

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# STATIC AND MEDIA
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),

# ADMIN
    url(r'^admin12345/', include(admin.site.urls)),

# SMART HOUSE
    url(r'^grafiks/', include('grafiks.urls')),
    url(r'^', include('pieraksts.urls')),

]
