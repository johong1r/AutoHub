from django.db import models


class Cars(models.Model):
    picture = models.ImageField(null=True, blank=True, verbose_name='Фотография')
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