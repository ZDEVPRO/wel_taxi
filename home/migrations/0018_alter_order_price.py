# Generated by Django 4.1.2 on 2022-10-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_archiveorder_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(default=100000, max_length=200),
        ),
    ]
