from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("logout/", logout_user, name="logout"),
    path("about/", about_user, name="about"),
    path("update/", update_profile, name="update"),
    path("", home, name="home"),
    path("skills/", user_skills, name="skills"),
    path("exp/", exp, name="exp")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)