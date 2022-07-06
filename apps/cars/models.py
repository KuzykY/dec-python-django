from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from apps.autopark.models import AutoParkModel

from .enums import RegEx

# from .managers import CarManager


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=30,
                             validators=[RegexValidator(RegEx.BRAND.pattern,RegEx.BRAND.msg)])
    price = models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(100000)])
    year = models.IntegerField(validators=[MinValueValidator(1980),MaxValueValidator(2022)])
    auto_park=models.ForeignKey(AutoParkModel,on_delete=models.CASCADE,related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects=CarManager()
