from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tren/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/$', 'pieraksts.views.tren'), # treneris choise


    url(r'^atcelt/(?P<id>\w+\-\w+\-\w+\-\w+\-\w+)/$', 'pieraksts.views.cancel'), # pieraksta atcelshana
    url(r'^atcelts/(?P<id>\w+\-\w+\-\w+\-\w+\-\w+)/$', 'pieraksts.views.cancel_ok'), # pieraksta atcelshana


    url(r'^pieraksts/(?P<g_id>\d+)/$', 'pieraksts.views.pieraksts'), # pieraksts


    url(r'^select/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/any/$', 'pieraksts.views.any'), # any trainer
    url(r'^select/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/(?P<t_id>\w+|\w+\-\w+|\w+\-\w+)/$', 'pieraksts.views.specific'), # specific trainer


    url(r'^', 'pieraksts.views.home'),

]

