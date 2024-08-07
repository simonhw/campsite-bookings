from . import views
from django.urls import path

urlpatterns = [
    path('', views.booking_view,
         name='booking'),
    path('manage-bookings/', views.AllBookings.as_view(),
         name='manage_bookings'),
    path('my-bookings/', views.UserBookings.as_view(),
         name='user_bookings'),
    path('my-bookings/edit/<str:id>', views.booking_edit,
         name='booking_edit'),
    path('my-bookings/delete/<str:id>', views.booking_delete,
         name='booking_delete'),
    path('manage-bookings/delete/<str:id>', views.booking_delete,
         name='booking_delete'),
]
