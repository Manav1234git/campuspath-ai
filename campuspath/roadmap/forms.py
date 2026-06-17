from django import forms
from .models import Roadmap


class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ["title", "target_role", "duration_months"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: AI Engineer Roadmap"
            }),
            "target_role": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: AI Engineer"
            }),
            "duration_months": forms.NumberInput(attrs={
                "class": "form-control"
            }),
        }