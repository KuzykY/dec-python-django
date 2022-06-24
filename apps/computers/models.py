from django.db import models


class ComputerModel(models.Model):
    class Meta:
        db_table = 'Computers'

    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    ram = models.IntegerField()
    monitor_inches = models.IntegerField()
