# Generated by Django 4.1.2 on 2022-12-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='new_app/static')),
            ],
        ),
    ]
