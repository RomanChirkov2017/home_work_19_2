from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(**NULLABLE, verbose_name='Цена за шт.')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Номер версии')
    name = models.CharField(max_length=250, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(self.id)
        if self.is_active:
            Version.objects.filter(product=self.product).exclude(id=self.id).update(is_active=False)



    def __str__(self):
        return f'{self.name} {self.version_number} ({self.product})'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


class Blog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.name} ({self.create_date})'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
