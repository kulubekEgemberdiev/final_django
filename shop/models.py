from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    trademark = models.CharField(max_length=50, verbose_name='Торговая марка')
    maker = models.CharField(max_length=50, verbose_name='Производитель')
    image = models.CharField(max_length=250, verbose_name='Ссылка на изображение')
    qty_in_stock = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    product_type = models.CharField(max_length=50, verbose_name='Тип товара')

    def __str__(self):
        return f"{self.id}. {self.name}"

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    category = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return f"{self.category}"

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
