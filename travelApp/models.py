from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.
class Customer(models.Model):
    middle_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    def last_name(self):
        return self.user.last_name
    def email(self):
        return self.user.email

class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Airport(models.Model):
    departure_name = models.CharField(max_length=255)
    arrival_name = models.CharField(max_length=255)
    IATA_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.departure_name} > {self.arrival_name}'

class Flight(models.Model):
    FLIGHT_CLASS_BUSINESS = 'B'
    FLIGHT_CLASS_ECONOMY = 'E'
    FLIGHT_CLASS_CHOICES = [
        (FLIGHT_CLASS_BUSINESS, 'B'),
        (FLIGHT_CLASS_ECONOMY, 'E')
    ]
    flight_number = models.CharField(max_length=50)
    checking_time = models.DateTimeField(max_length=255)
    departure_time = models.DateTimeField(max_length=255)
    arrival_time = models.DateTimeField(max_length=255)
    duration_in_min = models.PositiveSmallIntegerField()
    flight_class = models.CharField(max_length=1, choices=FLIGHT_CLASS_CHOICES, default=FLIGHT_CLASS_ECONOMY)
    airport = models.ForeignKey(Airport, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.flight_number


class Booking(models.Model):
    ticket_number = models.CharField(max_length=50)
    confirmation_number = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    issue_date = models.DateTimeField(max_length=255)
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)


class Airline(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    airport = models.ForeignKey(Airport, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name