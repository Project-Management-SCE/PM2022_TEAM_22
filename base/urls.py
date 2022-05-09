from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    # path("upgrade_vip_page/", views.upgrade_vip_page, name="upgrade_vip_page"),
    path("upgrade_vip/", views.upgrade_vip, name="upgrade_vip"),
    path("upgrade_platinum/", views.upgrade_platinum, name="upgrade_platinum"),
    path("register/", views.registerPage, name="register"),
    path("", views.home, name="home"),
    path("change_password/", views.change_password, name="change_password"),
    path("change_username/", views.change_username, name="change_username"),
    path("definition/", views.definition, name="definition"),
    path("search_results/", views.search_results, name="search_results"),
    path("trending/", views.trending, name="trending"),
    path("about/", views.about, name="about"),
    # path("room/<str:pk>", views.room, name="room"),
]
