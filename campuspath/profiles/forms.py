from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "full_name",
            "university",
            "branch",
            "semester",
            "target_role",
            "bio",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "university": forms.TextInput(attrs={"class": "form-control"}),
            "branch": forms.TextInput(attrs={"class": "form-control"}),
            "semester": forms.NumberInput(attrs={"class": "form-control"}),
           "target_role": forms.TextInput(attrs={
    "class": "form-control",
    "placeholder": "Example: AI Engineer, Backend Developer, DevOps Engineer"
}),
            "bio": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }