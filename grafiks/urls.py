from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Reception Cancel
    url(r'^cancel/(?P<g_id>\d+)/(?P<p_id>\d+)/$', 'grafiks.views.reception_cancel'),


# Nodarbibas
    url(r'^nod/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.nod_list', name='nod_list'),
    url(r'^canceled/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.cancel_list'),
    url(r'^day/(?P<d_id>\d+)/$', 'grafiks.views.day_list', name='day_list'),

# Login
    url(r'^login/$', 'grafiks.views.login'),
    url(r'^logout/$', 'grafiks.views.logout'),

# Nodarbibu dzeshana
    url(r'^plan/(?P<w_id>\d+)/$', 'grafiks.views.week_list', name="nod_plan"),
    url(r'^plan/(?P<w_id>\d+)/cancel/(?P<g_id>\d+)/$', 'grafiks.views.graf_cancel'),
    url(r'^plan/$', 'grafiks.views.graf_list'),

# Nodarbibas pievienoshana
    url(r'^add/$', 'grafiks.views.graf_add'),

# Main --> Shodienas nodarbibas
    url(r'^$', 'grafiks.views.main'),

]
