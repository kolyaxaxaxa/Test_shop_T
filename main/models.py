from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='SEO_URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='SEO_URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
