from django.conf.urls import patterns, include, url
from login.views import *
from . import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^add_question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
                        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
                        url(r'^/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
                        url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', logout_page),
                        url(r'^add_question/search/$', views.search, name="search"),

                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       # If user is not login it will redirect to login page
                       url(r'^register/$', register),
                       url(r'^register/success/$', register_success),
                       url(r'^home/$', home),
                       url(r'^add_question/$', views.add_question, name='add_question'),
                       )