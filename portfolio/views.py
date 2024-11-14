from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .pdf import html2pdf
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.

@login_required(login_url="login/")
def home(request):
    about = AboutUser.objects.filter(user=request.user)
    exp = UserExperience.objects.filter(user=request.user)
    skills = UserSkills.objects.filter(user=request.user)
    current_year = datetime.now().year

    context = {"title" : "Portfolio Project", "about" : about, "skills" : skills, "exp" : exp, "year" : current_year}
    return render(request, "portfolio/index.html", context)

def register_user(request):
    page = "register"
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
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
    user = request.user.aboutuser
    form = AboutForm(instance=user)

    if request.method == "POST":
        form = AboutForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = AboutForm(instance=user)

    context = {"form" : form, "user" : user}
    return render(request, "portfolio/update_profile.html", context)

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
def update_skills(request, pk):
    skill = UserSkills.objects.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = SkillForm(instance=skill)

    context = {"form" : form}
    return render(request, "portfolio/edit_skills.html", context)

@login_required(login_url="login/")
def delete_skill(request, pk):
    skill = UserSkills.objects.get(id=pk)

    skill.delete()
    return redirect("home")

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

@login_required(login_url="login/")
def update_exp(request, pk):
    exp = UserExperience.objects.get(id=pk)
    form = ExperienceForm(instance=exp)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = ExperienceForm(instance=exp)

    context = {"form" : form}
    return render(request, "portfolio/update_exp.html", context)

@login_required(login_url="login/")
def delete_exp(request, pk):
    exp = UserExperience.objects.get(id=pk)

    exp.delete()
    return redirect("home")

@login_required(login_url="login/")
def view_cv(request):
    about = AboutUser.objects.filter(user=request.user)
    skill = UserSkills.objects.filter(user=request.user)
    exp = UserExperience.objects.filter(user=request.user)
    context_dict = {
        "user" : request.user,
        "about" : about,
        "skill" : skill,
        "exp" : exp
    }
    pdf = html2pdf("portfolio/cv.html", context_dict)

    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        file_name = "cv.pdf"
        content = f"inline; filename={file_name}"
        response["Content-Disposition"] = content
        return response
    else:
        return Http404("PDF file doesn't exist")
    