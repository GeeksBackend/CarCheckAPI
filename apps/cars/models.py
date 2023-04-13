from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Car(models.Model):
    license_plate = models.CharField(
        verbose_name="Гос номер", #01KG111AAA
        max_length=10, null=True, 
        unique=True
    )
    brand = models.CharField(
        verbose_name="Марка",
        max_length=200
    )
    model = models.CharField(
        verbose_name="Модель",
        max_length=200
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска"
    )
    color = models.CharField(
        verbose_name="Цвет",
        max_length=100
    )
    rudder_location = models.CharField(
        verbose_name="Расположение руля",
        max_length=100
    )
    engine_volume = models.PositiveSmallIntegerField(
        verbose_name="Объем двигателя"
    )

    def __str__(self):
        return f"{self.brand}, {self.model}, {self.license_plate}"
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

class SpecialMarks(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE,
        related_name="cars_special_marks"
    )
    title = models.CharField(
        verbose_name="Отметка",
        max_length=255
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Особая отметка"
        verbose_name_plural = "Особые отметки"

class PeriodsOwnership(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE,
        related_name="cars_periods_ownership"
    )
    from_date = models.DateField(
        verbose_name="От",
        auto_now_add=True
    )
    before_date = models.DateField(
        verbose_name="До",
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.from_date} {self.before_date}"
    
    class Meta:
        verbose_name = "Период владения"
        verbose_name_plural = "Периоды владения"

class CarPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="users_posts",
        verbose_name="Пользователь"
    )
    brand = models.CharField(
        verbose_name="Марка",
        max_length=200
    )
    model = models.CharField(
        verbose_name="Модель",
        max_length=200
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска"
    )
    color = models.CharField(
        verbose_name="Цвет",
        max_length=100
    )
    rudder_location = models.CharField(
        verbose_name="Расположение руля",
        max_length=100
    )
    engine_volume = models.PositiveSmallIntegerField(
        verbose_name="Объем двигателя",
        blank=True, null=True
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        blank=True, null=True
    )
    mileage = models.PositiveIntegerField(
        verbose_name="Пробег",
        blank=True, null=True
    )
    transmission = models.CharField(
        max_length=100,
        verbose_name="Коробка передач",
        blank=True, null=True
    )
    region = models.CharField(
        max_length=255,
        verbose_name="Регион",
        blank=True, null=True
    )
    accounting = models.CharField(
        max_length=200,
        verbose_name="Учёт",
        blank=True, null=True
    )
    another = models.CharField(
        max_length=500,
        verbose_name="Прочее"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"