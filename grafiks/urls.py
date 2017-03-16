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

#    url(r'^tren/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/', 'pieraksts.views.tren'), # treneris choise

#    url(r'^pieraksts/(?P<g_id>\d+)/', 'pieraksts.views.pieraksts'), # pieraksts

#    url(r'^select/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/any/', 'pieraksts.views.any'), # any trainer
#    url(r'^select/(?P<n_id>\w+|\w+\-\w+|\w+\-\w+\-\w+)/(?P<t_id>\w+|\w+\-\w+|\w+\-\w+)/', 'pieraksts.views.specific'), # specific trainer


    url(r'^nod/(?P<g_id>\d+)/', 'grafiks.views.nod_list'),
    url(r'^cancel/(?P<g_id>\d+)/', 'grafiks.views.cancel_list'),
    url(r'^', 'grafiks.views.main'),

]


