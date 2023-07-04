from django.db import models
from django.utils import timezone

class Car(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    car_brand = models.CharField(max_length=100, null=True)
    car_model = models.CharField(max_length=100, null=True)
    plate_number = models.CharField(max_length=20)

class ParkingFee(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField(null=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2, null=True)


