# Generated by Django 4.1.7 on 2023-03-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0004_auto_20180701_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(default='1', primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
