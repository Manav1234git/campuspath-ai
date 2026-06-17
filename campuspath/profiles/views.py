from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ProfileSkillForm
from .models import Profile, ProfileSkill


@login_required
def create_profile(request):
    if Profile.objects.filter(user=request.user).exists():
        return redirect("my_profile")

    if request.method == "POST":
        form = ProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("my_profile")
    else:
        form = ProfileForm()

    return render(request, "profiles/create_profile.html", {"form": form})


@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "profiles/my_profile.html", {"profile": profile})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("my_profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profiles/edit_profile.html", {"form": form})


@login_required
def delete_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profile.delete()
        return redirect("dashboard")

    return render(request, "profiles/delete_profile.html", {"profile": profile})

@login_required
def my_skills(request):
    profile = Profile.objects.get(user=request.user)
    skills = ProfileSkill.objects.filter(profile=profile)

    return render(request, "profiles/my_skills.html", {"skills": skills})


@login_required
def add_skill(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfileSkillForm(request.POST)

        if form.is_valid():
            profile_skill = form.save(commit=False)
            profile_skill.profile = profile
            profile_skill.save()
            return redirect("my_skills")
    else:
        form = ProfileSkillForm()

    return render(request, "profiles/add_skill.html", {"form": form})


@login_required
def delete_skill(request, pk):
    profile = Profile.objects.get(user=request.user)
    profile_skill = ProfileSkill.objects.get(id=pk, profile=profile)

    if request.method == "POST":
        profile_skill.delete()
        return redirect("my_skills")

    return render(request, "profiles/delete_skill.html", {"profile_skill": profile_skill})

@login_required
def edit_skill(request, pk):
    profile = Profile.objects.get(user=request.user)
    profile_skill = ProfileSkill.objects.get(id=pk, profile=profile)

    if request.method == "POST":
        form = ProfileSkillForm(request.POST, instance=profile_skill)

        if form.is_valid():
            form.save()
            return redirect("my_skills")
    else:
        form = ProfileSkillForm(instance=profile_skill)

    return render(request, "profiles/edit_skill.html", {"form": form})