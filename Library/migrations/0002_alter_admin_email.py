# Generated by Django 4.1.1 on 2022-09-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
