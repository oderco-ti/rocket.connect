# Generated by Django 3.2.13 on 2022-11-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instance', '0020_alter_connector_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='default_messages',
            field=models.JSONField(blank=True, default=dict, help_text='Default Messages to load at the Rocket.Connect App', null=True),
        ),
    ]