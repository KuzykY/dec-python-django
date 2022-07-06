from django.core.validators import RegexValidator
from django.db import models

from .enums import RegEx


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'autopark'

    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
