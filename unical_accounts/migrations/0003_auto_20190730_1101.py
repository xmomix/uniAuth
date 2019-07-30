# Generated by Django 2.2.2 on 2019-07-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unical_accounts', '0002_auto_20190730_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='origin',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='from which conenctor this user come from'),
        ),
        migrations.AlterField(
            model_name='user',
            name='original_uid',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Username used in connectors auth'),
        ),
    ]
