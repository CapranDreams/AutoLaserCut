# Generated by Django 4.1.6 on 2023-02-10 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autolasercut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolpaths',
            name='user',
        ),
    ]
