from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from accounts.permissions import IsAdmin, IsCustomer

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
        """Admin can update the status only."""
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)
