# Generated by Django 3.0.3 on 2020-02-14 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='blogs',
        ),
    ]
