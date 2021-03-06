# Generated by Django 3.0.6 on 2020-05-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_pickup',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='message',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='notification',
        ),
        migrations.AddField(
            model_name='booking',
            name='order_type',
            field=models.CharField(choices=[('b', 'buy_in'), ('p', 'pick_up')], default='b', max_length=1),
        ),
    ]
