# Generated by Django 3.1.4 on 2020-12-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='menu_description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
