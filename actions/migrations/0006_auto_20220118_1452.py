# Generated by Django 3.1.7 on 2022-01-18 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
        ('actions', '0005_auto_20220118_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='entity',
        ),
        migrations.AddField(
            model_name='action',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions_action_entity', to='entity.entity'),
        ),
    ]