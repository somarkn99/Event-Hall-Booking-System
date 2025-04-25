from django.urls import path
from .views import PaymentCreateView, MyPaymentsListView, AllPaymentsListView

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='payment-create'),
    path('my-payments/', MyPaymentsListView.as_view(), name='payment-my-list'),
    path('all/', AllPaymentsListView.as_view(), name='payment-all-list'),
]
