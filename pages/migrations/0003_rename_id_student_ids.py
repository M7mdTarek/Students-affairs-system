# Generated by Django 4.0.4 on 2022-05-25 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_ida_student_id_rename_department_student_dep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Id',
            new_name='Ids',
        ),
    ]