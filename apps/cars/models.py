from django.db import models

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
        return self.brand 
    
    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"