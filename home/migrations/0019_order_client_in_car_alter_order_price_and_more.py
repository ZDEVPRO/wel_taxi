# Generated by Django 4.1.2 on 2022-10-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_in_car',
            field=models.CharField(default='Yo`q', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(default='Kelishiladi', max_length=200),
        ),
        migrations.AlterField(
            model_name='temporder',
            name='price',
            field=models.CharField(default='Kelishiladi', max_length=200),
        ),
    ]
