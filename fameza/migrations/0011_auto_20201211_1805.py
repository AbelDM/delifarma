# Generated by Django 3.1.4 on 2020-12-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fameza', '0010_auto_20201211_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
