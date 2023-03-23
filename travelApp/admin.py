from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Customer)
class CustomerAmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'phone', 'email']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name_istartswith']

class BookingInline(admin.TabularInline):
    model = models.Booking
    extra = 0
@admin.register(models.Passenger)
class passengerAdmin(admin.ModelAdmin):
    #inlines = [BookingInline]
    list_display = ['first_name', 'middle_name', 'last_name', 'nationality']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
@admin.register(models.Flight)
class flightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'checking_time', 'departure_time', 'arrival_time', 'flight_class', 'airport']
    list_editable = ['flight_class']

@admin.register(models.Booking)
class bookingAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'confirmation_number', 'issue_date', 'passenger', 'flight', 'price']

@admin.register(models.Airport)
class airportAdmin(admin.ModelAdmin):
    list_display = ['departure_name', 'arrival_name', 'IATA_code']

@admin.register(models.Airline)
class airlineAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'airport']
