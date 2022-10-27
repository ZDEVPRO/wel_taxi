# Generated by Django 4.1.2 on 2022-10-23 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='blacklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='black_list', to=settings.AUTH_USER_MODEL),
        ),
    ]