# Generated by Django 4.2.1 on 2023-05-07 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollingunit',
            old_name='result_1',
            new_name='APC',
        ),
        migrations.RenameField(
            model_name='pollingunit',
            old_name='result_2',
            new_name='LP',
        ),
        migrations.RenameField(
            model_name='pollingunit',
            old_name='result_3',
            new_name='PDP',
        ),
        migrations.RenameField(
            model_name='pollingunit',
            old_name='result_4',
            new_name='others',
        ),
    ]
