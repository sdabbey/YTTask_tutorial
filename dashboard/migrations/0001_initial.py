# Generated by Django 4.2.3 on 2023-07-29 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=500)),
                ('value', models.FloatField()),
                ('secret_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YTTasker_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.task')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
