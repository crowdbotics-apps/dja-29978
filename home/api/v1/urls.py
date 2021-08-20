from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ExercisesViewSet,
    Workout_AssignmentsViewSet,
    Workout_ExercisesViewSet,
    WorkoutsViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("workouts", WorkoutsViewSet)
router.register("exercises", ExercisesViewSet)
router.register("workout_exercises", Workout_ExercisesViewSet)
router.register("workout_assignments", Workout_AssignmentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
