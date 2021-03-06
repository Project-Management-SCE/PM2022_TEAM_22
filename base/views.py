from os import getenv
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import requests


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
            user.backend = "django.contrib.auth.backends.ModelBackend"
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


# change user name (not finished)
@login_required(login_url="login")
def change_username(request):
    if request.method == "POST":
        new_username = request.POST.get("username")
        if User.objects.filter(username=new_username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "base/change_username.html", {})

        else:
            user = User.objects.get(username=request.user.username)
            user.username = new_username
            user.save()

    return render(request, "base/change_username.html", {})


@login_required(login_url="login")
def definition(request):
    context = {}
    return render(request, "base/definition.html", context)


@login_required(login_url="login")
def trending(request):
    context = {}
    url = "https://yfapi.net/v1/finance/trending/US"
    headers = {"x-api-key": getenv("API_TOKEN")}
    response = requests.request("GET", url, headers=headers)
    temp = response.json()["finance"]["result"][0]["quotes"]
    arr = []
    for i, c in enumerate(temp):
        arr.append(c["symbol"])
    context = {"response": arr}

    return render(request, "base/trending.html", context)


# SEARCH RESULTS
@login_required(login_url="login")
def search_results(request):
    if request.method == "POST":
        q = request.POST.get("query")
        quote_url = "https://yfapi.net/v6/finance/quote"
        quoteSummary_url = (
            "https://yfapi.net/v11/finance/quoteSummary/" + q + "?lang=en&region=US&modules=defaultKeyStatistics"
        )
        querystring = {"symbols": q}
        headers = {"x-api-key": getenv("API_TOKEN")}
        try:
            response = requests.request("GET", quote_url, headers=headers, params=querystring)         
            response_beta = requests.request("GET", quoteSummary_url, headers=headers, params=querystring)
            context = {"query": q, "response": response.json()["quoteResponse"]["result"][0]}
            earn = response_beta.json()["quoteSummary"]["result"][0]["defaultKeyStatistics"]
            beta = response_beta.json()["quoteSummary"]["result"][0]["defaultKeyStatistics"]["beta"]
            
            context["earn"] = earn["earningsQuarterlyGrowth"]["fmt"]
            context["splitdate"] = earn["lastSplitDate"]["fmt"]
            if beta:
                context["beta"] = beta["raw"]
            else:
                context["beta"] = "NOT FOUND"

            url2 = f"https://yfapi.net/v11/finance/quoteSummary/{q}?lang=en&region=US&modules=defaultKeyStatistics%2CassetProfile"
            url3 = f"https://yfapi.net/v6/finance/recommendationsbysymbol/{q}"
            responseSummary = requests.request("GET", url2, headers=headers, params=querystring)
            dictSummary = {"sum": responseSummary.json()["quoteSummary"]["result"][0]["assetProfile"]}
            context.update(dictSummary)
            response3 = requests.request("GET", url3, headers=headers, params=querystring)
            dictRecommended = {"recommended": response3.json()["finance"]["result"][0]["recommendedSymbols"]}
            context.update(dictRecommended)
            return render(request, "base/search_results.html", context)
        
        except (IndexError, KeyError, TypeError):
             return render(request, "base/error_page.html")
    else:
        return render(request, "base/home.html")


def home(request):
    context = {}
    return render(request, "base/home.html", context)


@login_required(login_url="login")
def upgrade_vip(request):
    group = Group.objects.get(name="vip")
    request.user.groups.set([group])
    return render(request, "base/upgrade_vip.html")


@login_required(login_url="login")
def upgrade_platinum(request):
    group = Group.objects.get(name="platinum")
    request.user.groups.set([group])
    return render(request, "base/upgrade_platinum.html")


@login_required(login_url="login")
def about(request):
    context = {}
    return render(request, "base/about.html", context)
