# Generated by Django 2.2.9 on 2020-03-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unical_accounts', '0008_auto_20200314_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='place_of_birth',
        ),
        migrations.AlterField(
            model_name='user',
            name='origin',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='from which connector this user come from'),
        ),
    ]