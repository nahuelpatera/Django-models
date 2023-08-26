# Generated by Django 3.2.2 on 2023-08-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('marvel_id', models.PositiveIntegerField(unique=True, verbose_name='marvel id')),
                ('title', models.CharField(default='', max_length=120, verbose_name='title')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('price', models.FloatField(default=0.0, max_length=5, verbose_name='price')),
                ('stock_qty', models.PositiveIntegerField(default=0, verbose_name='stock qty')),
                ('picture', models.URLField(default='', verbose_name='picture')),
            ],
            options={
                'verbose_name': 'comic',
                'verbose_name_plural': 'comics',
                'db_table': 'e_commerce_comics',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('favorite', models.BooleanField(default=False)),
                ('cart', models.BooleanField(default=False)),
                ('wished_qty', models.PositiveIntegerField(default=0, verbose_name='wished qty')),
                ('bought_qty', models.PositiveIntegerField(default=0, verbose_name='bought qty')),
            ],
            options={
                'verbose_name': 'wish list',
                'verbose_name_plural': 'wish_list',
                'db_table': 'e_commerce_wish_list',
            },
        ),
    ]