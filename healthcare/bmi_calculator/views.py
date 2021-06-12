from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from bmi_calculator.services import BmiCatRisk


class BmiCalculator(APIView):
	def post(self, request):
		return Response(BmiCatRisk.get_bmi_cat_risk(request.data))
