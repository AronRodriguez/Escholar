# Generated by Django 5.0.6 on 2024-05-11 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_course_board_passing_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('themecolor', models.CharField(max_length=100)),
                ('logoUrl', models.ImageField(upload_to='university_logos/')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='college',
        ),
        migrations.RemoveField(
            model_name='course',
            name='board_passing_rate',
        ),
        migrations.RemoveField(
            model_name='course',
            name='expected_tuition',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_start', models.DateField()),
                ('application_end', models.DateField()),
                ('entrance_exam_date', models.DateField()),
                ('university', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.university')),
            ],
        ),
        migrations.CreateModel(
            name='UniversityCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_tuition', models.DecimalField(decimal_places=2, max_digits=10)),
                ('board_passing_rate', models.DecimalField(decimal_places=2, max_digits=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.university')),
            ],
        ),
        migrations.DeleteModel(
            name='College',
        ),
    ]
