# Generated by Django 3.1.3 on 2020-11-23 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='date_aded',
            new_name='date_added',
        ),
    ]