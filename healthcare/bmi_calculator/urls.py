from django.urls import path
from .views import BmiCalculator

urlpatterns = [
    path('v0/bmi/', BmiCalculator.as_view(), name='bmi'),
]
