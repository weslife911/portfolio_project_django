from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.   
class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class AboutUser(models.Model):
    profile_image = models.ImageField(upload_to="user_images/", default="avatar.svg")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    birthday = models.CharField(max_length=30)
    experience = models.CharField(max_length=20)
    happy_clients = models.CharField(max_length=1000000000, null=True)
    complete_projects = models.CharField(max_length=100000000000, null=True)

    def __str__(self):
        return self.name

class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill = models.CharField(max_length=100, null=True)
    percentage_knowledge = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.skill
    
class UserExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=100)
    company_worked_for = models.CharField(max_length=100)
    period = models.CharField(max_length=100, null=True)
    job_description = models.TextField(blank=True)