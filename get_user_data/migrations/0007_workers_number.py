# Generated by Django 5.0.6 on 2024-05-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_user_data', '0006_remove_auto_manual_transmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='number',
            field=models.TextField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]
