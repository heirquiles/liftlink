# Generated by Django 4.1.5 on 2023-02-01 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lift_link', '0004_remove_newexercise_workouts_newworkout_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='newexercise',
            name='weight',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newexercise',
            name='notes',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]
