from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Payment
from .serializers import PaymentSerializer
from accounts.permissions import IsAdmin, IsCustomer
from bookings.models import Booking
from utils.email import send_notification_email


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def perform_create(self, serializer):
        booking_id = self.request.data.get('booking')
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            raise ValidationError("Booking not found.")

        if booking.user != self.request.user:
            raise ValidationError("You can only pay for your own bookings.")

        payment = serializer.save(amount=booking.total_price)

        send_notification_email(
            to_email=self.request.user.email,
            subject="Payment Confirmation 💳",
            message=f"Hello {self.request.user.full_name},\n\n"
                    f"We have successfully received your payment of {payment.amount} "
                    f"for booking #{booking.id} ({booking.hall.name}).\n\nThank you!"
        )


class MyPaymentsListView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Payment.objects.filter(booking__user=self.request.user)


class AllPaymentsListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
