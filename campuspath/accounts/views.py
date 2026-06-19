from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from profiles.models import Profile, ProfileSkill
from roadmap.models import Roadmap, Task, CourseRecommendation, ProjectRecommendation

def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "accounts/register.html",
                {"error": "Username already exists"}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    profile = Profile.objects.filter(user=request.user).first()

    total_skills = 0
    total_roadmaps = 0
    total_tasks = 0
    completed_tasks = 0
    completed_courses = 0
    completed_projects = 0
    overall_progress = 0

    if profile:
        total_skills = ProfileSkill.objects.filter(profile=profile).count()
        roadmaps = Roadmap.objects.filter(profile=profile)
        total_roadmaps = roadmaps.count()

        total_tasks = Task.objects.filter(milestone__roadmap__in=roadmaps).count()
        completed_tasks = Task.objects.filter(
            milestone__roadmap__in=roadmaps,
            is_completed=True
        ).count()

        completed_courses = CourseRecommendation.objects.filter(
            roadmap__in=roadmaps,
            is_completed=True
        ).count()

        completed_projects = ProjectRecommendation.objects.filter(
            roadmap__in=roadmaps,
            is_completed=True
        ).count()

        if total_tasks > 0:
            overall_progress = int((completed_tasks / total_tasks) * 100)

    context = {
        "profile": profile,
        "total_skills": total_skills,
        "total_roadmaps": total_roadmaps,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completed_courses": completed_courses,
        "completed_projects": completed_projects,
        "overall_progress": overall_progress,
    }

    return render(request, "accounts/dashboard.html", context)


def logout_view(request):
    auth.logout(request)
    return redirect("home")