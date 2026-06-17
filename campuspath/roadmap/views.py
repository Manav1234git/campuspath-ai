from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .models import Roadmap,Milestone
from .forms import RoadmapForm,MilestoneForm

@login_required
def my_roadmaps(request):
    profile = Profile.objects.get(user=request.user)
    roadmaps = Roadmap.objects.filter(profile=profile).order_by("-created_at")

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

    return render(
        request,
        "roadmap/roadmap_detail.html",
        {
            "roadmap": roadmap,
            "milestones": milestones,
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