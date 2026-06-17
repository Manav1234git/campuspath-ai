from django import forms
from .models import Roadmap, Milestone


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


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ["title", "description", "week_number"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "week_number": forms.NumberInput(attrs={"class": "form-control"}),
        }