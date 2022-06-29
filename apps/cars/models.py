from django.db import models
from django.core import validators

from apps.autopark.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=30,
                             validators=(validators.MaxLengthValidator(30), validators.MinLengthValidator(2)))
    price = models.IntegerField(validators=(validators.MinValueValidator(1000), validators.MaxValueValidator(100000)))
    year = models.IntegerField(validators=(validators.MinValueValidator(1980), validators.MaxValueValidator(2022)))
    auto_park=models.ForeignKey(AutoParkModel,on_delete=models.CASCADE,related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
