from django.conf.urls import patterns, url
from tt import views

urlpatterns = [
    url(r'^people/$', views.snippet_list),
    url(r'^people/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
