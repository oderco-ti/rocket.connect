# Generated by Django 3.1.7 on 2021-04-20 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instance', '0006_server_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='servers', to=settings.AUTH_USER_MODEL),
        ),
    ]
