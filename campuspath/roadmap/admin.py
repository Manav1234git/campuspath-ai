from django.contrib import admin
from .models import Roadmap, Milestone, Task, ProjectRecommendation, CourseRecommendation

admin.site.register(Roadmap)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(ProjectRecommendation)
admin.site.register(CourseRecommendation)