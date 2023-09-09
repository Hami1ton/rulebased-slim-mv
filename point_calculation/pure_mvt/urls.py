from django.urls import path
from .views import order, history


urlpatterns = [
    path("order", order, name="order"),
    path("history", history, name="history"),
]
