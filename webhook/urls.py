from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from webapp.views import GithubEventViewSet


router = routers.DefaultRouter()
router.register(r'github-events', GithubEventViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += router.urls
