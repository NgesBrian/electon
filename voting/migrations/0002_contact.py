# Generated by Django 2.0.6 on 2018-06-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('idContact', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=80)),
            ],
        ),
    ]
