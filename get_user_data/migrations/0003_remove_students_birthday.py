# Generated by Django 5.0.6 on 2024-05-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_user_data', '0002_remove_students_fillial_students_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='birthday',
        ),
    ]
