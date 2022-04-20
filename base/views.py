from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User ,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse


# Create your views here.


def loginPage(request):
    page = "login"
    context = {"page": page}
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except BaseException:
            messages.error(request, "User does not exist")
            return render(request, "base/login_register.html", context)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password isn't valid")

    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("home")


def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Registeration failed")
    context = {"form": form}
    return render(request, "base/login_register.html", context)


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("change_password")
        else:
            messages.error(request, "Error when changing password.")
    form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "base/change_password.html", context)


def home(request):
    # rooms = Room.objects.all()
    # context = {"rooms": rooms}
    context = {}
    return render(request, "base/home.html", context)

def upgrade_vip_page(request):
    context = {}
    return render(request, "base/upgrade_vip_page.html", context)


def upgrade_vip(request):
    group=Group.objects.get(name='vip')
    print(11)
    request.user.groups.add(group)
    print(111)
    Group.objects.get(name="vip")

    context = {}
    print(1)
    g =None
    if request.user.groups.exists():
       print(2)
       g = request.user.groups.all()[0].name
    print(3)
    if g == 'vip' :
       return HttpResponse('it is vip')
    else:
        return render(request, "base/home.html", context)

# @login_required(login_url="login")
# def room(request, pk):
#     room = Room.objects.get(id=pk)
#     context = {"room": room}
#     return render(request, "base/room.html", context)
