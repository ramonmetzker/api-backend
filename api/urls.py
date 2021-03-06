from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ClienteViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
