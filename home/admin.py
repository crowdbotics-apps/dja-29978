from django.contrib import admin
from .models import Exercises, Workout_Assignments, Workout_Exercises, Workouts

admin.site.register(Workouts)
admin.site.register(Exercises)
admin.site.register(Workout_Exercises)
admin.site.register(Workout_Assignments)

# Register your models here.
