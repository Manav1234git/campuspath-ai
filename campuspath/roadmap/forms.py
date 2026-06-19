from django import forms
from .models import Roadmap, Milestone, Task, CourseRecommendation, ProjectRecommendation


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

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: Learn Python OOP"
            }),
        }

class CourseRecommendationForm(forms.ModelForm):
    class Meta:
        model = CourseRecommendation
        fields = ["title", "platform", "link"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "platform": forms.TextInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
        }

class ProjectRecommendationForm(forms.ModelForm):
    class Meta:
        model = ProjectRecommendation
        fields = ["title", "description", "difficulty_level"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "difficulty_level": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Example: Beginner, Intermediate, Advanced"
            }),
        }