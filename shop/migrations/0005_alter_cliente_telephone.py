# Generated by Django 4.1.7 on 2023-03-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]