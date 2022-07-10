# Generated by Django 3.2.7 on 2021-09-19 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('done', models.BooleanField(default=False, verbose_name='Звонок выполнен')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Описание категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('image', models.ImageField(default='', upload_to='img/categories', verbose_name='Фото категории')),
                ('url', models.CharField(default='', max_length=200, verbose_name='Ссылка на страницу категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование компании-продавца')),
                ('description', models.TextField(verbose_name='Описание компании-продавца')),
                ('contacts', models.TextField(verbose_name='Контакты')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(default='', upload_to='img/products', verbose_name='Фото товара')),
                ('category', models.ManyToManyField(to='shop.Category', verbose_name='Категории')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.seller', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Залоговок отзыва')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('creator', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Оставитель отзыва')),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_stars', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'unique_toотзgether': {('creator', 'product')},
            },
        ),
    ]
