class BmiCatRisk:
	@staticmethod
	def get_bmi_cat_risk(request_data):
		response_data = []
		for record in request_data:
			heightm = record.get("HeightCm") / 100
			record["BMI"] = round(record.get("WeightKg") / (heightm * heightm))
			if record["BMI"] <= 18.4:
				record["Category"] = "Underweight"
				record["Health risk"] = "Malnutrition risk"
			elif record["BMI"] <= 24.9:
				record["Category"] = "Normal weight"
				record["Health risk"] = "Low risk"
			elif record["BMI"] <= 29.9:
				record["Category"] = "Overweight"
				record["Health risk"] = "Enhanced risk"
			elif record["BMI"] <= 34.9:
				record["Category"] = "Moderately obese"
				record["Health risk"] = "Medium risk"
			elif record["BMI"] <= 39.9:
				record["Category"] = "Severely obese"
				record["Health risk"] = "High risk"
			else:
				record["Category"] = "Very severely obese"
				record["Health risk"] = "Very high risk"
			response_data.append(record)

		return response_data
