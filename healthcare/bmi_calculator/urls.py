from django.urls import path
from .views import BmiCalculator, CategoryCount

urlpatterns = [
    path('v0/bmi/', BmiCalculator.as_view()),
    path('v0/overwight/', CategoryCount.as_view()),
]
