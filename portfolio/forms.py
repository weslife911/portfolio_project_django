from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2"
        ]

    def __int__(self):
        super().__init__()
        for field in self.fields.values():
            field.label = None

class AboutForm(ModelForm):
    class Meta:
        model = AboutUser
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "phone" : TextInput(attrs={"placeholder" : "+237 6XX XX XX XX"}),
            "address" : TextInput(attrs={"placeholder" : "123 Street, New York, USA"}),
            "birthday" : TextInput(attrs={"placeholder" : "1 April 1990"}),
            "experience" : TextInput(attrs={"placeholder" : "10 Years"}),
            "degree" : TextInput(attrs={"placeholder" : "Masters"}),
            "happy_clients" : TextInput(attrs={"placeholder" : "100"}),
            "complete_projects" : TextInput(attrs={"placeholder" : "200"}),
        }

class SkillForm(ModelForm):
    class Meta:
        model = UserSkills
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "skill" : TextInput(attrs={"placeholder" : "HTML"}),
            "percentage_knowledge" : TextInput(attrs={"placeholder" : "75%"}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = UserExperience
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            "role" : TextInput(attrs={"placeholder" : "Web Designer"}),
            "company_worked_for" : TextInput(attrs={"placeholder" : "Microsoft"}),
            "period" : TextInput(attrs={"placeholder" : "2000-2004"}),
        }