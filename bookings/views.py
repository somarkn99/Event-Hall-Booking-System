from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from accounts.permissions import IsAdmin, IsCustomer
from utils.email import send_notification_email

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingListCustomerView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class BookingListAdminView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class BookingUpdateStatusView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    lookup_field = 'pk'

    def partial_update(self, request, *args, **kwargs):
        booking = self.get_object()
        response = super().partial_update(request, *args, **kwargs)

        new_status = request.data.get("status")
        if new_status == "Confirmed":
            send_notification_email(
                to_email=booking.user.email,
                subject="Your Booking Confirmation",
                template_name='emails/booking_confirmed.html',
                context={
                    'user_name': booking.user.full_name,
                    'hall_name': booking.hall.name,
                    'plain_message': f"Hello {booking.user.full_name},\n\nYour booking for {booking.hall.name} has been confirmed."
                }
            )
        elif new_status == "Cancelled":
            send_notification_email(
                to_email=booking.user.email,
                subject="Your Booking Cancellation",
                template_name='emails/booking_cancelled.html',
                context={
                    'user_name': booking.user.full_name,
                    'hall_name': booking.hall.name,
                    'plain_message': f"Hello {booking.user.full_name},\n\nYour booking for {booking.hall.name} has been cancelled."
                }
            )
        return response
