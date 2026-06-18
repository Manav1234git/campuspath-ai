from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .models import Roadmap, Milestone, Task, CourseRecommendation
from .forms import RoadmapForm, MilestoneForm, TaskForm, CourseRecommendationForm
from django.utils import timezone

@login_required
def my_roadmaps(request):
    profile = Profile.objects.get(user=request.user)
    roadmaps = Roadmap.objects.filter(profile=profile).order_by("-created_at")

    for roadmap in roadmaps:
        total_tasks = Task.objects.filter(milestone__roadmap=roadmap).count()
        completed_tasks = Task.objects.filter(
            milestone__roadmap=roadmap,
            is_completed=True
        ).count()

        roadmap.progress = 0
        if total_tasks > 0:
            roadmap.progress = int((completed_tasks / total_tasks) * 100)

    return render(request, "roadmap/my_roadmaps.html", {"roadmaps": roadmaps})


@login_required
def create_roadmap(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = RoadmapForm(request.POST)

        if form.is_valid():
            roadmap = form.save(commit=False)
            roadmap.profile = profile
            roadmap.save()
            return redirect("my_roadmaps")
    else:
        form = RoadmapForm(initial={"target_role": profile.target_role})

    return render(request, "roadmap/create_roadmap.html", {"form": form})

@login_required
def roadmap_detail(request, pk):
    profile = Profile.objects.get(user=request.user)
    roadmap = Roadmap.objects.get(id=pk, profile=profile)
    milestones = Milestone.objects.filter(roadmap=roadmap).order_by("week_number")
    courses = CourseRecommendation.objects.filter(roadmap=roadmap)

    total_tasks = Task.objects.filter(milestone__roadmap=roadmap).count()
    completed_tasks = Task.objects.filter(
        milestone__roadmap=roadmap,
        is_completed=True
    ).count()

    progress = 0

    if total_tasks > 0:
        progress = int((completed_tasks / total_tasks) * 100)

    return render(
        request,
        "roadmap/roadmap_detail.html",
        {
            "roadmap": roadmap,
            "milestones": milestones,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress": progress,
            "courses": courses,
        }
    )


@login_required
def add_milestone(request, roadmap_id):
    profile = Profile.objects.get(user=request.user)
    roadmap = Roadmap.objects.get(id=roadmap_id, profile=profile)

    if request.method == "POST":
        form = MilestoneForm(request.POST)

        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.roadmap = roadmap
            milestone.save()
            return redirect("roadmap_detail", pk=roadmap.id)
    else:
        form = MilestoneForm()

    return render(request, "roadmap/add_milestone.html", {"form": form, "roadmap": roadmap})


@login_required
def edit_milestone(request, pk):
    profile = Profile.objects.get(user=request.user)
    milestone = Milestone.objects.get(id=pk, roadmap__profile=profile)

    if request.method == "POST":
        form = MilestoneForm(request.POST, instance=milestone)

        if form.is_valid():
            form.save()
            return redirect("roadmap_detail", pk=milestone.roadmap.id)
    else:
        form = MilestoneForm(instance=milestone)

    return render(request, "roadmap/edit_milestone.html", {"form": form})


@login_required
def delete_milestone(request, pk):
    profile = Profile.objects.get(user=request.user)
    milestone = Milestone.objects.get(id=pk, roadmap__profile=profile)
    roadmap_id = milestone.roadmap.id

    if request.method == "POST":
        milestone.delete()
        return redirect("roadmap_detail", pk=roadmap_id)

    return render(request, "roadmap/delete_milestone.html", {"milestone": milestone})

@login_required
def add_task(request, milestone_id):
    profile = Profile.objects.get(user=request.user)
    milestone = Milestone.objects.get(id=milestone_id, roadmap__profile=profile)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.milestone = milestone
            task.save()
            return redirect("roadmap_detail", pk=milestone.roadmap.id)
    else:
        form = TaskForm()

    return render(request, "roadmap/add_task.html", {"form": form, "milestone": milestone})


@login_required
def toggle_task(request, pk):
    profile = Profile.objects.get(user=request.user)
    task = Task.objects.get(id=pk, milestone__roadmap__profile=profile)

    task.is_completed = not task.is_completed

    if task.is_completed:
        task.completed_at = timezone.now()
    else:
        task.completed_at = None

    task.save()
    return redirect("roadmap_detail", pk=task.milestone.roadmap.id)


@login_required
def delete_task(request, pk):
    profile = Profile.objects.get(user=request.user)
    task = Task.objects.get(id=pk, milestone__roadmap__profile=profile)
    roadmap_id = task.milestone.roadmap.id

    if request.method == "POST":
        task.delete()
        return redirect("roadmap_detail", pk=roadmap_id)

    return render(request, "roadmap/delete_task.html", {"task": task})

@login_required
def edit_task(request, pk):
    profile = Profile.objects.get(user=request.user)
    task = Task.objects.get(id=pk, milestone__roadmap__profile=profile)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("roadmap_detail", pk=task.milestone.roadmap.id)
    else:
        form = TaskForm(instance=task)

    return render(request, "roadmap/edit_task.html", {"form": form})

@login_required
def edit_roadmap(request, pk):
    profile = Profile.objects.get(user=request.user)
    roadmap = Roadmap.objects.get(id=pk, profile=profile)

    if request.method == "POST":
        form = RoadmapForm(request.POST, instance=roadmap)

        if form.is_valid():
            form.save()
            return redirect("roadmap_detail", pk=roadmap.id)
    else:
        form = RoadmapForm(instance=roadmap)

    return render(request, "roadmap/edit_roadmap.html", {"form": form})


@login_required
def delete_roadmap(request, pk):
    profile = Profile.objects.get(user=request.user)
    roadmap = Roadmap.objects.get(id=pk, profile=profile)

    if request.method == "POST":
        roadmap.delete()
        return redirect("my_roadmaps")

    return render(request, "roadmap/delete_roadmap.html", {"roadmap": roadmap})

@login_required
def add_course(request, roadmap_id):
    profile = Profile.objects.get(user=request.user)
    roadmap = Roadmap.objects.get(id=roadmap_id, profile=profile)

    if request.method == "POST":
        form = CourseRecommendationForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.roadmap = roadmap
            course.save()
            return redirect("roadmap_detail", pk=roadmap.id)
    else:
        form = CourseRecommendationForm()

    return render(request, "roadmap/add_course.html", {"form": form, "roadmap": roadmap})


@login_required
def edit_course(request, pk):
    profile = Profile.objects.get(user=request.user)
    course = CourseRecommendation.objects.get(id=pk, roadmap__profile=profile)

    if request.method == "POST":
        form = CourseRecommendationForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("roadmap_detail", pk=course.roadmap.id)
    else:
        form = CourseRecommendationForm(instance=course)

    return render(request, "roadmap/edit_course.html", {"form": form})


@login_required
def delete_course(request, pk):
    profile = Profile.objects.get(user=request.user)
    course = CourseRecommendation.objects.get(id=pk, roadmap__profile=profile)
    roadmap_id = course.roadmap.id

    if request.method == "POST":
        course.delete()
        return redirect("roadmap_detail", pk=roadmap_id)

    return render(request, "roadmap/delete_course.html", {"course": course})