# Generated by Django 4.0.6 on 2022-09-05 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_alter_character_clase'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alineamiento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
