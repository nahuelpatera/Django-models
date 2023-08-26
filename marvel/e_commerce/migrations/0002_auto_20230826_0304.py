# Generated by Django 3.2.2 on 2023-08-26 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='comic',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='e_commerce.comic', verbose_name='comic'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='user_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]