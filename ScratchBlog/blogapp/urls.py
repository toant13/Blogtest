'''
Created on Oct 16, 2013

@author: toant
'''
from django.conf.urls import patterns, url

from blogapp import views


urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
                       
)