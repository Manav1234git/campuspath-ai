from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from .models import Roadmap
from .forms import RoadmapForm


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