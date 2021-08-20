from django.conf import settings
from django.db import models


class Workouts(models.Model):
    "Generated Model"
    name = models.TextField()
    trainer = models.OneToOneField(
        "users.Trainer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="workouts_trainer",
    )


class Exercises(models.Model):
    "Generated Model"
    name = models.TextField()
    description = models.TextField(
        null=True,
        blank=True,
    )


class Workout_Exercises(models.Model):
    "Generated Model"
    exercise = models.OneToOneField(
        "home.Exercises",
        on_delete=models.CASCADE,
        related_name="workout_exercises_exercise",
    )
    workout = models.OneToOneField(
        "home.Workouts",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="workout_exercises_workout",
    )
    reps = models.IntegerField(
        null=True,
        blank=True,
    )


class Workout_Assignments(models.Model):
    "Generated Model"
    workout = models.OneToOneField(
        "home.Workouts",
        on_delete=models.CASCADE,
        related_name="workout_assignments_workout",
    )
    user = models.OneToOneField(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="workout_assignments_user",
    )
