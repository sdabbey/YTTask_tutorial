# Generated by Django 4.2.3 on 2023-07-30 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_nofication_amount_remove_nofication_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nofication',
            new_name='Notification',
        ),
    ]
