from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^nod/(?P<g_id>\d+)/', 'grafiks.views.nod_list'),
    url(r'^cancel/(?P<g_id>\d+)/', 'grafiks.views.cancel_list'),
    url(r'^login/', 'grafiks.views.login'),
    url(r'^plan/', 'grafiks.views.nod_list'),
    url(r'^', 'grafiks.views.main'),

]
