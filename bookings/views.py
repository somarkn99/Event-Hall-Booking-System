from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from accounts.permissions import IsAdmin, IsCustomer
from utils.email import send_notification_email
from utils.responses import success_response, error_response

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomer]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(user=self.request.user)
            return success_response(
                message="Booking created successfully",
                data=BookingSerializer(booking).data,
                status_code=status.HTTP_201_CREATED
            )
        return error_response(
            message="Failed to create booking",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )

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
        serializer = self.get_serializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            booking = serializer.save()

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

            return success_response(
                message="Booking status updated successfully",
                data=BookingSerializer(booking).data
            )

        return error_response(
            message="Failed to update booking status",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )
