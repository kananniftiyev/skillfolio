# Generated by Django 5.0.3 on 2024-04-16 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.URLField(blank=True),
        ),
    ]
