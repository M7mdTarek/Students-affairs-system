# Generated by Django 4.0.4 on 2022-05-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_student_level_alter_student_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SuperUser',
        ),
        migrations.AlterField(
            model_name='student',
            name='dep',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
