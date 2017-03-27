from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Nodarbibas
    url(r'^nod/(?P<g_id>\d+)/', 'grafiks.views.nod_list'),
    url(r'^cancel/(?P<g_id>\d+)/', 'grafiks.views.cancel_list'),

# Login
    url(r'^login/', 'grafiks.views.login'),
    url(r'^logout/', 'grafiks.views.logout'),

# Grafika izmainjas
    url(r'^plan/(?P<w_id>\d+)/', 'grafiks.views.week_list'),
    url(r'^plan/', 'grafiks.views.graf_list'),

# Main --> Shodienas nodarbibas
    url(r'^', 'grafiks.views.main'),

]
