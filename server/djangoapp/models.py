# server/djangoapp/models.py

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Dodatna polja po želji, npr. country
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # choices za tip auta
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # možeš dodati više tipova po potrebi
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # M:N veza (1 make → više modela)
    dealer_id = models.IntegerField()  # povezuje se s dealerom iz Cloudant DB
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    # dodatno polje po želji
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
