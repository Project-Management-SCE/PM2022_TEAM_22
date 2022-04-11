from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("", views.home, name="home"),
    path("change_password/", views.change_password, name="change_password"),
    # path("room/<str:pk>", views.room, name="room"),
]
