from django.urls import path
from .views import ResponseViewset
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'server', ResponseViewset, basename = 'server')
urlpatterns = [] + router.urls
