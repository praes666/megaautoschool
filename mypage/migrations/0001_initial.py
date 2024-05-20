# Generated by Django 5.0.6 on 2024-05-18 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('get_user_data', '0003_remove_students_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('password', models.TextField()),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='get_user_data.students')),
            ],
        ),
    ]