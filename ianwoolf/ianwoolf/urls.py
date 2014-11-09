# admin form model
from django.conf.urls import patterns, include, url
from django.contrib import admin
# rest
from django.conf.urls import url, include
from rest_framework import routers
from tt import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^rs/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^add_db/', 'tt.views.home'),
#    url(r'^blog/', include('blog.urls')),
    url(r'^tt/',include('tt.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


