from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('airport/', views.airport, name='airport'),
    path('airline/', views.airline, name='airline'),
    path('passenger/', views.passenger, name='passenger'),
    path('flight/', views.flight, name='flight'),
    path('booking/', views.booking, name='booking'),
    path('<int:id>/edit_passenger/', views.editPassenger, name='edit'),
    path('<int:id>/delete_passenger', views.deletePassenger, name='delete'),
    path('<int:id>/edit_booking/', views.editBooking, name='edit2'),
    path('<int:id>/booking/', views.ticket, name='ticket'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_user, name='logout')
]