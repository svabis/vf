from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Login
    url(r'^login/$', 'grafiks.views.login'),
    url(r'^logout/$', 'grafiks.views.logout'),

# Reception History
    url(r'^hist/$', 'grafiks.views.history'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/$', 'grafiks.views.hist_date', name='hist_date'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/(?P<g_id>\d+)/p/$', 'grafiks.views.hist_date_kli'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/(?P<g_id>\d+)/c/$', 'grafiks.views.hist_date_cancel'),

# Reception Pieraksts
    url(r'^pierakstities/(?P<d_id>\d+)/(?P<n_id>\d+)/$', 'grafiks.views.reception_pieraksts'),
# Reception Cancel
    url(r'^cancel/(?P<d_id>\d+)/(?P<g_id>\d+)/(?P<p_id>\d+)/$', 'grafiks.views.reception_cancel'),

# Nodarbibas
    url(r'^nod/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.nod_list', name='nod_list'),
    url(r'^atteikumi/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.cancel_list'),
    url(r'^day/(?P<d_id>\d+)/$', 'grafiks.views.day_list', name='day_list'),
# Reception Print
    url(r'^print_nod/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.print_nod'),

# Nodarbibu dzeshana
    url(r'^plan/(?P<w_id>\d+)/$', 'grafiks.views.week_list', name="nod_plan"),
    url(r'^plan/(?P<w_id>\d+)/cancel/(?P<g_id>\d+)/$', 'grafiks.views.graf_cancel'),
    url(r'^plan/$', 'grafiks.views.graf_list'),

# Nodarbibas pievienoshana
    url(r'^add/$', 'grafiks.views.graf_add'),

# Treneru aizvietosan
    url(r'^tren/(?P<w_id>\d+)/$', 'grafiks.views.tren_week_list', name="nod_plan"),
    url(r'^tren/(?P<w_id>\d+)/cancel/(?P<g_id>\d+)/$', 'grafiks.views.tren_aizv'),
    url(r'^tren/$', 'grafiks.views.tren_list'),

# Main --> Shodienas nodarbibas
    url(r'^$', 'grafiks.views.main'),

]
