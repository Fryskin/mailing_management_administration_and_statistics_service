# Generated by Django 4.2.3 on 2023-08-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_a_s', '0006_clientofservice_is_relevant_clientofservice_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientofservice',
            name='is_relevant',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='relevant status'),
        ),
    ]