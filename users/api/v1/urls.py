from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TrainerViewSet

router = DefaultRouter()
router.register("trainer", TrainerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
