from django.contrib import admin
from .models import Exercises, Workout_Exercises, Workouts

admin.site.register(Workouts)
admin.site.register(Exercises)
admin.site.register(Workout_Exercises)

# Register your models here.
