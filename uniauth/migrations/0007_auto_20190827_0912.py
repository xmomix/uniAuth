# Generated by Django 2.2.2 on 2019-08-27 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uniauth', '0006_auto_20190827_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='encrypt_saml_responses',
            new_name='encrypt_assertions',
        ),
    ]