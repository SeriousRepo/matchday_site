# Generated by Django 2.1.2 on 2018-11-08 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_teaminmatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teaminmatch',
            name='external_identifier',
        ),
    ]
