from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tt import views

urlpatterns = [
    url(r'^people/$', views.snippet_list),
    url(r'^people/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^3people/$', views.PeopleList.as_view()),
    url(r'^3people/(?P<pk>[0-9]+)/$', views.PeopleDetail.as_view()),
    url(r'^32people/$', views.PeopleList2.as_view()),
    url(r'^32people/(?P<pk>[0-9]+)/$', views.PeopleDetail2.as_view()),
    url(r'^33people/$', views.PeopleList3.as_view()),
    url(r'^33people/(?P<pk>[0-9]+)/$', views.PeopleDetail3.as_view()),
    url(r'^my/$', 'tt.views.myown'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
