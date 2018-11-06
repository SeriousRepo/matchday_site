# Generated by Django 2.1.2 on 2018-10-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_identifier', models.IntegerField(unique=True)),
                ('external_identifier', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('area_id', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_identifier', models.IntegerField(unique=True)),
                ('external_identifier', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('role', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50, null=True)),
                ('shirt_number', models.IntegerField(null=True)),
                ('external_team_identifier', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_identifier', models.IntegerField(unique=True)),
                ('external_identifier', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]