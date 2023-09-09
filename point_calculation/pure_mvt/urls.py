from django.urls import path
from .views import point, history


urlpatterns = [
    path("point", point, name="point"),
    path("history", history, name="history"),
]
