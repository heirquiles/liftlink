# Generated by Django 4.1.5 on 2023-02-01 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lift_link', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='NewExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reps', models.IntegerField()),
                ('sets', models.IntegerField()),
                ('notes', models.CharField(max_length=240)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workouts', models.ManyToManyField(to='lift_link.newworkout')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
