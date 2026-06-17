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
    "skill_name": forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Example: Python, Django, Java, Machine Learning"
    }),
    "proficiency_level": forms.Select(attrs={"class": "form-select"}),
}


from .models import Profile, ProfileSkill


class ProfileSkillForm(forms.ModelForm):
    class Meta:
        model = ProfileSkill
        fields = ["skill_name", "proficiency_level"]

        widgets = {
            "skill": forms.Select(attrs={"class": "form-select"}),
            "proficiency_level": forms.Select(attrs={"class": "form-select"}),
        }