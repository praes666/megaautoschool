# Generated by Django 5.0.6 on 2024-05-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_user_data', '0008_auto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='drive_hours',
            field=models.PositiveIntegerField(default=60),
        ),
    ]
