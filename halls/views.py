from rest_framework import generics, permissions
from .models import Hall
from .serializers import HallSerializer
from accounts.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class HallListView(generics.ListAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location', 'capacity', 'price_per_hour']
    search_fields = ['name', 'description', 'location']
    ordering_fields = ['price_per_hour', 'capacity']
    ordering = ['price_per_hour']

class HallDetailView(generics.RetrieveAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.AllowAny]

class HallCreateView(generics.CreateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HallUpdateView(generics.UpdateAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Hall.objects.filter(owner=self.request.user)

class HallDeleteView(generics.DestroyAPIView):
    queryset = Hall.objects.all()
    serializer_class = HallSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Hall.objects.filter(owner=self.request.user)
