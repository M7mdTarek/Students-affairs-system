# Generated by Django 4.0.4 on 2022-05-24 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=2)),
                ('ida', models.IntegerField()),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=5)),
                ('level', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
            ],
            options={
                'ordering': ['-gpa'],
            },
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
