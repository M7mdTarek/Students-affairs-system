# Generated by Django 4.0.4 on 2022-05-25 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='ida',
            new_name='Id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='department',
            new_name='dep',
        ),
    ]
