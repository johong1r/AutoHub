from django.db import models

from django_resized import ResizedImageField
from accounts.models import User


class Cars(models.Model):
    picture = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)
    name = models.CharField(max_length=100, verbose_name="Название")
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name="Модель")
    price = models.IntegerField(verbose_name="Цена")
    body = models.ForeignKey("Body", on_delete=models.CASCADE, max_length=100, verbose_name="Кузов")
    color = models.CharField(max_length=100, verbose_name="Цвет")
    seats = models.PositiveIntegerField(verbose_name="Количество мест")
    sale = models.ForeignKey("Sale", on_delete=models.CASCADE, verbose_name='Покупка', null=True, blank=True)
    rent = models.ForeignKey("Rent", on_delete=models.CASCADE, verbose_name='Аренда', null=True, blank=True)
    transmission = models.ForeignKey("Transmission", on_delete=models.CASCADE, verbose_name='Коробка передач')
    year = models.IntegerField(verbose_name="Год")
    description = models.CharField(max_length=1000, verbose_name="Описание")
    join_date = models.DateField(verbose_name='дата присоединения', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Sale(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return f'{self.id} - {self.name}'
    

class Rent(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'

    def __str__(self):
        return f'{self.id} - {self.name}'
    

class Transmission(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'

    def __str__(self):
        return f'{self.id} - {self.name}'
    

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    logo = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return f'{self.id} - {self.name}'


class Body(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'

    def __str__(self):
        return f'{self.id} - {self.name}'
    

class OrderItem(models.Model):
    cars = models.ForeignKey(Cars, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество', default=1)
    price = models.IntegerField(verbose_name='Цена')
    cart = models.ForeignKey('Order', verbose_name='Корзина', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f'OrderItem: {self.goods.name} (x{self.quantity})'
    

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    user = models.ForeignKey(OrderItem, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order #{self.id} - {self.items}'