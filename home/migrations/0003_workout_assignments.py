# Generated by Django 2.2.24 on 2021-08-20 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_exercises_workout_exercises_workouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout_Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workout_assignments_user', to=settings.AUTH_USER_MODEL)),
                ('workout', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workout_assignments_workout', to='home.Workouts')),
            ],
        ),
    ]