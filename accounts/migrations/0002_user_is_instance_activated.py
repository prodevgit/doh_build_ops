# Generated by Django 3.1.7 on 2022-01-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_instance_activated',
            field=models.BooleanField(default=False),
        ),
    ]
