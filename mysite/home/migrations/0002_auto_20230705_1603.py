# Generated by Django 3.0.14 on 2023-07-05 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]