from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

@login_required(login_url="login/")
def home(request):
    about = AboutUser.objects.all()
    exp = UserExperience.objects.all()
    skills = UserSkills.objects.all()

    context = {"title" : "Portfolio Project", "about" : about, "skills" : skills, "exp" : exp}
    return render(request, "portfolio/index.html", context)

def register_user(request):
    page = "register"
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("about")
        else:
            form = RegistrationForm()
            messages.error(request, "Invalid email or passwords don't match!!!")

    context = {"page" : page, "form" : form, "title" : "Registration"}
    return render(request, "portfolio/auth.html", context)

def login_user(request):
    page = "login"

    email = request.POST.get("email")
    password = request.POST.get("password")

    if request.method == "POST":
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Credentials invalid!!!")

    context = {"page" : page, "title" : "Login"}
    return render(request, "portfolio/auth.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")

def about_user(request):
    form = AboutForm()

    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.user = request.user
            current_user.save()
            return redirect("home")
            
        print(request.user)

    context = {"title" : "About", "form" : form}
    return render(request, "portfolio/about.html", context)

@login_required(login_url="login/")
def update_profile(request):
    form = AboutForm(instance=request.user)
    profile, created = AboutUser.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = AboutForm(instance=request.user)

    context = {"form" : form}
    return render(request, "portfolio/update.html", context)

@login_required(login_url="login/")
def user_skills(request):
    skill_form = SkillForm()

    if request.method == "POST":
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_owner = skill_form.save(commit=False)
            skill_owner.user = request.user
            skill_owner.save()
            return redirect("home")
            
        else:
            skill_form = SkillForm()

    context = {"skill_form" : skill_form}
    return render(request, "portfolio/skill.html", context)

@login_required(login_url="login/")
def exp(request):
    form = ExperienceForm()

    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            current_user.user = request.user
            current_user.save()
            return redirect("home")
        else:
            form = ExperienceForm()

    context = {"form" : form}
    return render(request, "portfolio/exp.html", context)