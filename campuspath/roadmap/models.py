from django.db import models
from profiles.models import Profile


class Roadmap(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    target_role = models.CharField(max_length=100)
    duration_months = models.PositiveIntegerField(default=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    week_number = models.PositiveIntegerField()

    def __str__(self):
        return f"Week {self.week_number}: {self.title}"


class Task(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class ProjectRecommendation(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class CourseRecommendation(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    platform = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title