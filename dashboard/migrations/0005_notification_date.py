# Generated by Django 4.2.3 on 2023-07-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_nofication_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
