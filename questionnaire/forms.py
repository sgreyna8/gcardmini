from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [
            "id",
            "store_name",
            "balance",
            "balance_currency",
            "price",
            "price_currency",
            "network",
            "method",
            "address",
            "gcard_no",
            "gcard_pin",
            "email"
        ]