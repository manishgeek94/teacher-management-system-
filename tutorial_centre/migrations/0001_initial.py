# Generated by Django 3.1.7 on 2021-02-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=50)),
                ('teacher_subjects', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('teacher_alloted', models.ManyToManyField(to='tutorial_centre.Teacher')),
            ],
        ),
    ]