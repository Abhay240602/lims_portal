# Generated by Django 5.0.7 on 2024-07-29 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lims_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reader',
            old_name='refernce_id',
            new_name='reference_id',
        ),
    ]
