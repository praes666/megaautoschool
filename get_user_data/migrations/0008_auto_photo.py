# Generated by Django 5.0.6 on 2024-05-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_user_data', '0007_workers_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='photo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
