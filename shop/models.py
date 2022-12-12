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


class Cart(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE,
                                verbose_name='Товары', related_name='product_in_cart')
    qty = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return f'{self.product.name} - {self.qty}'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def get_product_total(self):
        return self.qty * self.product.price

    @classmethod
    def get_total(cls):
        total = 0
        for cart in cls.objects.all():
            total += cart.get_product_total()
        return total


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    products = models.ManyToManyField('shop.Products', related_name='orders', verbose_name='Товары',
                                      through='shop.OrderProduct', through_fields=['order', 'product'])

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderProduct(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE,
                                verbose_name='Товар', related_name='order_products')
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              verbose_name='Заказ', related_name='order_products')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.product.name} - {self.order.name}'

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'