from django.urls import path

from .views.rulebased_calc_view import RulebasedCalcView
from .views.pure_mvt_calc_view import PureMvtCalcView


urlpatterns = [
    path("", PureMvtCalcView.as_view(), name="point"),
    path("point", PureMvtCalcView.as_view()),
    path("point-rule", RulebasedCalcView.as_view(), name="point-rule"),
]
