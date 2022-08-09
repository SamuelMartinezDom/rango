# Generated by Django 4.0.6 on 2022-08-09 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='parentesco',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='age',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
