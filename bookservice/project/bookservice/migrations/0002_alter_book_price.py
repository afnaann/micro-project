# Generated by Django 5.1.3 on 2024-11-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
