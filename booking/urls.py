from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view, name='booking'),
    path('my-bookings/', views.UserBookings.as_view(), name='user_bookings' ),
    path('my-bookings/edit/<str:id>', views.booking_edit, name='booking_edit'),
]