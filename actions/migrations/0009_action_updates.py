# Generated by Django 3.1.7 on 2022-02-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_actionupdate'),
        ('actions', '0008_action_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='updates',
            field=models.ManyToManyField(blank=True, to='comments.ActionUpdate'),
        ),
    ]