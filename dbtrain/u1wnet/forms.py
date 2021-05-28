from django import forms
from .models import Un1model, TrainingData, ValidationData

class Un1modelForm(forms.ModelForm):
    class Meta:
        model = Un1model
        fields = [
            'name',
            'version',
        ]