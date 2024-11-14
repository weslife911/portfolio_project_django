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
    path("update-profile/", update_profile, name="update-profile"),
    path("", home, name="home"),
    path("skills/", user_skills, name="skills"),
    path("update-skills/<str:pk>/", update_skills, name="update-skills"),
    path("delete-skill/<str:pk>/", delete_skill, name="delete-skill"),
    path("exp/", exp, name="exp"),
    path("update-exp/<str:pk>/", update_exp, name="update-exp"),
    path("delete-exp/<str:pk>", delete_exp, name="delete-exp"),
    path("cv/", view_cv, name="cv"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)