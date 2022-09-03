# Generated by Django 4.1 on 2022-08-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MEANING',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_of_speech', models.CharField(max_length=30)),
                ('origin', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=300)),
                ('synonyms', models.CharField(max_length=200)),
                ('antonyms', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WORDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Date_added', models.DateTimeField()),
            ],
        ),
    ]
