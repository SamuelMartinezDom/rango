# Generated by Django 4.0.6 on 2022-08-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('clase', models.CharField(max_length=13)),
                ('lvl', models.IntegerField()),
            ],
        ),
    ]
