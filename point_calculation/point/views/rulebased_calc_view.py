from django.shortcuts import render
from django.views.generic import View
from ..forms import PointCalculationForm
from .point_rule_engine import point_engine


class RulebasedCalcView(View):
    def get(self, request):
        f = PointCalculationForm()
        return render(request, "point-rule.html", {"form": f} )

    def post(self, request):
        f = PointCalculationForm(request.POST)
        if f.is_valid():
            point = self.calculate(f)

            return render(request, "point-rule.html", {
                "form": f,
                "point": 1
                })
    
    def calculate(self, form_data):
        """
        calculate Points by the PointCalculationForm infomation  
        """
        return point_engine.calculate_point()
        
