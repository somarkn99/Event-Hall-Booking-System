from django.urls import path
from .views import BookingCreateView, BookingListCustomerView, BookingListAdminView, BookingUpdateStatusView

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('my-bookings/', BookingListCustomerView.as_view(), name='booking-customer-list'),
    path('all/', BookingListAdminView.as_view(), name='booking-admin-list'),
    path('<int:pk>/update-status/', BookingUpdateStatusView.as_view(), name='booking-update-status'),
]
