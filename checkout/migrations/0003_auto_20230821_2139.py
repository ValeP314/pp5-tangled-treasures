# Generated by Django 3.2.20 on 2023-08-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
    ]
