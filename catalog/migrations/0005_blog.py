# Generated by Django 5.0.1 on 2024-02-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_category_name_alter_product_change_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=200, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('view_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
        ),
    ]
