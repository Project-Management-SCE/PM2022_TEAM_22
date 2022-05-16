from django.test import TestCase
from django.contrib.auth.models import User
from .models import Favorite
import requests
from django.urls import reverse

# Create your tests here.
class FavoriteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        Favorite.objects.create(name="apple", user=self.user)

    def test_animals_can_speak(self):
        apple_fav = Favorite.objects.get(user=self.user, name="apple")
        self.assertEqual(apple_fav.user.username, "testuser")
        self.assertEqual(apple_fav.name, "apple")


class queryTestCase(TestCase):
    q = "msft"
    url = "https://yfapi.net/v6/finance/quote"
    beta_url = "https://yfapi.net/v11/finance/quoteSummary/" + q + "?lang=en&region=US&modules=defaultKeyStatistics"
    recommendUrl = "https://yfapi.net/v6/finance/recommendationsbysymbol/" + q
    querystring = {"symbols": q}
    headers = {"x-api-key": "3KPyUUzNRS8O1o5sTVrip2ZZlRkxu5UP5gxgVscR"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_beta = requests.request("GET", beta_url, headers=headers, params=querystring)
        context = {"query": q, "response": response.json()["quoteResponse"]["result"][0]}
        responserecommend = requests.request("GET", recommendUrl, headers=headers, params=querystring)
        dictRecommended = {"recommended": responserecommend.json()["finance"]["result"][0]["recommendedSymbols"]}
        beta = response_beta.json()["quoteSummary"]["result"][0]["defaultKeyStatistics"]["beta"]
        summary = response_beta.json()["quoteSummary"]["result"][0]["defaultKeyStatistics"]
        beta = summary["beta"]
        earn = summary["earningsQuarterlyGrowth"]
        if beta:
            context["beta"] = beta["raw"]
        else:
            context["beta"] = "NOT FOUND"

        if earn:
            context["earn"] = earn["fmt"]
        else:
            context["earn"] = "NOT FOUND"

        def test_fiftyTwoWeekLow(self):
            self.assertIn("fiftyTwoWeekLow", self.context.get("response").keys())

        def test_fiftyTwoWeekHigh(self):
            self.assertIn("fiftyTwoWeekHigh", self.context.get("response").keys())

        def test_beta(self):
            self.assertIn("beta", self.context.keys())

        def test_regularMarketDayLow(self):
            self.assertIn("regularMarketDayLow", self.context.get("response").keys())

        def test_regularMarketDayHigh(self):
            self.assertIn("regularMarketDayHigh", self.context.get("response").keys())

        def test_DayVolume(self):
            self.assertIn("regularMarketVolume", self.context.get("response").keys())

        def test_MarketCap(self):
            self.assertIn("marketCap", self.context.get("response").keys())

        def test_earningsQuarterlyGrowth(self):
            self.assertIn("earn", self.context.keys())
        
        def test_marketLocation(self):
            self.assertIn("market", self.context.get("response").keys())



    except (requests.exceptions.RequestException, KeyError) as e:
        print(e)

class templateTestCase(TestCase):
    try:
        def test_url_template_about(self): #Checking redirection
            response = self.client.get(reverse("about"))
            self.assertEqual(response.status_code, 302)
        
        def test_url_template_change_password(self): #Checking redirection
            response = self.client.get(reverse("change_password"))
            self.assertEqual(response.status_code, 302)

        def test_url_template_change_username(self): #Checking redirection
            response = self.client.get(reverse("change_username"))
            self.assertEqual(response.status_code, 302)

        def test_url_template_definition(self): #Checking redirection
            response = self.client.get(reverse("definition"))
            self.assertEqual(response.status_code, 302)

        def test_url_template_home(self): # Checking url
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)

        def test_url_template_login_register(self): #Checking url
            response = self.client.get(reverse("login"))
            self.assertEqual(response.status_code, 200)
        
        def test_url_template_login_register(self): #Checking url
            response = self.client.get(reverse("register"))
            self.assertEqual(response.status_code, 200)

        def test_url_template_trending(self): #Checking redirection
            response = self.client.get(reverse("trending"))
            self.assertEqual(response.status_code, 302)

    except (requests.exceptions.RequestException, KeyError) as e:
        print(e)