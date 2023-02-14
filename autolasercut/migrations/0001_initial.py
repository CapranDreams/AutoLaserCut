# Generated by Django 4.1.6 on 2023-02-10 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toolpaths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('toolpath', models.FileField(upload_to='toolpaths')),
                ('filename', models.FilePathField(path='toolpaths')),
                ('vectorlength', models.FloatField(default=0.0)),
                ('vectortype', models.CharField(max_length=10)),
                ('moddate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]