from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Flight
from .models import Passenger
from .models import Booking
from .flight import TicketForm
from.passenger import PassengerForm, EditPassengerForm
from .booking import BookingForm, EditBookingForm
from .airline import AirlineForm
from .airport import AirportForm

# Create your views here.

def index(request):
    flight = Flight.objects.all()

    return render(request, 'index.html', {
        'flight':flight
    })

@login_required
def airport(request):
    if request.method == "POST":
        airport = AirportForm(request.POST, request.FILES)
        if airport.is_valid():
            airport.save()

            return redirect('/airport')
    else:
        airport = AirportForm


    return render(request, 'airport.html', {
        'airport':airport
    })

@login_required
def airline(request):
    if request.method == "POST":
        airline = AirlineForm(request.POST, request.FILES)
        if airline.is_valid():
            airline.save()

            return redirect('/airline')
    else:
        airline = AirlineForm


    return render(request, 'airline.html', {
        'airline':airline
    })

@login_required
def passenger(request):

    query = request.GET.get('query', '')
    passengers = Passenger.objects.all()

    if request.method == "POST":
        passenger = PassengerForm(request.POST, request.FILES)
        if passenger.is_valid():
            passenger.save()

            return redirect('/passenger')
    else:
        passenger = PassengerForm

    if query:
        passengers = Passenger.objects.filter(Q(first_name__icontains=query) | Q(phone__icontains=query) | Q(passport_number__icontains=query))


    return render(request, 'passenger.html', {
        'passenger':passenger,
        'passengers': passengers,
        'query': query
    })

@login_required
def flight(request):
    if request.method == "POST":
        flight = TicketForm(request.POST, request.FILES)
        if flight.is_valid():
            flight.save()

            return redirect('/flight')
    else:
        flight = TicketForm


    return render(request, 'flight.html', {
        'flight':flight
    })
@login_required
def booking(request):
    bookings = Booking.objects.all()
    if request.method == "POST":
        booking = BookingForm(request.POST, request.FILES)
        if booking.is_valid():
            booking.save()

            return redirect('/booking')
    else:
        booking = BookingForm


    return render(request, 'booking.html', {
        'booking':booking,
        'bookings': bookings
    })

@login_required
def editBooking(request, id):
    booking = get_object_or_404(Booking, pk=id)

    if request.method == "POST":
        booking = EditBookingForm(request.POST, request.FILES, instance=booking)

        if booking.is_valid():
            booking.save()

            return redirect('booking')
    else:
        booking = EditBookingForm(instance=booking)


    return render(request, 'booking.html', {
        'booking':booking
    })


@login_required
def editPassenger(request, id):
    passenger = get_object_or_404(Passenger, pk=id)

    if request.method == "POST":
        passenger = EditPassengerForm(request.POST, request.FILES, instance=passenger)

        if passenger.is_valid():
            passenger.save()

            return redirect('passenger')
    else:
        passenger = EditPassengerForm(instance=passenger)


    return render(request, 'passenger.html', {
        'passenger':passenger
    })

@login_required
def deletePassenger(request, id):
    deletedPassenger = get_object_or_404(Passenger, pk=id)
    deletedPassenger.delete()

    return redirect('passenger')

@login_required
def ticket(request, id):
    passenger = Passenger.objects.get(pk=id)
    booking = Booking.objects.select_related('passenger').get(pk=id)
    flight =  Flight.objects.get(id=id)

    context = {
        'passenger':passenger,
        'booking': booking,
        'flight': flight
    }

    return render(request, 'ticket.html', context)

def logout_user(request):
    logout(request)

    return redirect('login')