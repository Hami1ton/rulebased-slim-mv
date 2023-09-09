from django.urls import path
from .views.pure_mvt_calc_view import history, PureMvtCalcView


urlpatterns = [
    path("", PureMvtCalcView.as_view(), name="point"),
    path("point", PureMvtCalcView.as_view()),
    path("history", history, name="history"),
]
