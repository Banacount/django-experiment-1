from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-imo/", views.createImoPage, name="create-imo-page"),
    path("register/", views.registerPage, name="register-page"),
    path("login/", views.loginPage, name="login-page"),
    path("personal/", views.userPersonal, name="user-personal-info"),
    path("logout/", views.logoutPage, name="logout-page")
]
