from rest_framework import routers
from userapi.views import UserViewSet
from django.urls import path
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # other paths
    path(r'auth/', include('rest_auth.urls')),
    path(r'', include(router.urls)),
]
#    path(r'', include(router.urls)),
# NameError: name 'path' is not defined; you should import them first
