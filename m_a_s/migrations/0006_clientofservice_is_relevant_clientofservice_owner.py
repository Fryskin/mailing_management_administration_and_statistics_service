# Generated by Django 4.2.3 on 2023-08-27 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('m_a_s', '0005_remove_clientofservice_newsletter_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientofservice',
            name='is_relevant',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='publish status'),
        ),
        migrations.AddField(
            model_name='clientofservice',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
