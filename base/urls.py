from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("", views.home, name="home"),
    path("change_password/", views.change_password, name="change_password"),
    path("change_username/", views.change_username, name="change_username"),
    path("definition/", views.definition, name="definition"),
    path("search_results/", views.search_results, name="search_results"),
    path("trending/", views.trending, name="trending"),

    # path("room/<str:pk>", views.room, name="room"),
]
