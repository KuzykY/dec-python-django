from django.db import models
from django.core import validators


class AutoParkModel(models.Model):
    class Meta:
        db_table='autopark'

    name=models.CharField(max_length=100,validators=(validators.MinLengthValidator(3),validators.MaxLengthValidator(30)))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
