# Generated by Django 4.0.4 on 2022-05-25 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_id_student_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Ids',
        ),
    ]
