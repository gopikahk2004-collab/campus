from django import forms
from .models import MaintenanceRequest

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['title', 'description', 'category', 'location', 'priority']

class MaintenanceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['status']
