from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


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