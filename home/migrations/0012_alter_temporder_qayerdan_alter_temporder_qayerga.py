# Generated by Django 4.1.2 on 2022-10-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_order_blacklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporder',
            name='qayerdan',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='temporder',
            name='qayerga',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
