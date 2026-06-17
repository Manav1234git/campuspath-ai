from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    branch = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    target_role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name





class ProfileSkill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    skill_name = models.CharField(max_length=100)

    proficiency_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES
    )

class Meta:
    unique_together = ('profile', 'skill_name')

    def __str__(self):
        return f"{self.profile.full_name} - {self.skill.name}"