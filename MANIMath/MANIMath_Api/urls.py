from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModelViewSet

router = DefaultRouter()
router.register(r'models', ModelViewSet, basename='models')

urlpatterns = [
    path('api/', include(router.urls)),
]