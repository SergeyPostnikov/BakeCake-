from django.db import models
from django.utils.timezone import localtime


class Cake(models.Model):
    NUMBER_LEVELS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ]
    FORM = [
        ('Круг', 'Круг'),
        ('Квадрат', 'Квадрат'),
        ('Прямоугольник', 'Прямоугольник')
    ]
    TOPPING = [
        ('Без', 'Без'),
        ('Белый соус', 'Белый соус'),
        ('Карамельный', 'Карамельный'),
        ('Кленовый', 'Кленовый'),
        ('Черничный', 'Черничный'),
        ('Молочный шоколад', 'Молочный шоколад'),
        ('Клубничный', 'Клубничный'),
    ]
    BERRIES = [
        ('Ежевика', 'Ежевика'),
        ('Малина', 'Малина'),
        ('Голубика', 'Голубика'),
        ('Клубника', 'Клубника'),
    ]
    DEKOR = [
        ('Фисташки', 'Фисташки'),
        ('Безе', 'Безе'),
        ('Фундук', 'Фундук'),
        ('Пекан', 'Пекан'),
        ('Маршмеллоу', 'Маршмеллоу'),
        ('Марципан', 'Марципан')
    ]

    cake_level = models.CharField(
            verbose_name='level', max_length=1, choices=NUMBER_LEVELS, default='1'
    )

    cake_form = models.CharField(
            verbose_name='form', max_length=20, choices=FORM
    )

    cake_topping = models.CharField(
            verbose_name='topping', max_length=50, choices=TOPPING
    )

    cake_berries = models.CharField(
            verbose_name='berries', max_length=20, blank = True, choices=BERRIES
    )

    cake_dekor = models.CharField(
            verbose_name='dekor', max_length=20, blank = True, choices=DEKOR
    )

    cake_inscription = models.CharField(
            verbose_name='inscription', max_length=100, blank = True
    )

    cake_comment = models.CharField(
            verbose_name='comment', max_length=255, blank = True
    )


    def __str__(self):
        return f'Cake {self.pk} '


class User(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    buyer_name = models.CharField('full name', max_length=100)
    buyer_mail = models.EmailField('mail', max_length=50)
    buyer_phone = models.CharField('phone number', max_length=25)
    buyer_date = models.DateField('order time', null=True)
    buyer_discount = models.CharField('promo code', max_length=10, blank = True)

    
    def __str__(self):
        return f'User {self.pk} '
