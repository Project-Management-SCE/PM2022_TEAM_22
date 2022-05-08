from django.test import TestCase
from django.contrib.auth.models import User
from .models import Favorite
import requests

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
    querystring = {"symbols": q}
    headers = {"x-api-key": "3KPyUUzNRS8O1o5sTVrip2ZZlRkxu5UP5gxgVscR"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_beta = requests.request("GET", beta_url, headers=headers, params=querystring)
        context = {"query": q, "response": response.json()["quoteResponse"]["result"][0]}
        beta = response_beta.json()["quoteSummary"]["result"][0]["defaultKeyStatistics"]["beta"]
        if beta:
            context["beta"] = beta["raw"]
        else:
            context["beta"] = "NOT FOUND"

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

        # def test_earningsQuarterlyGrowth(self):
        #     self.assertIn("earningsQuarterlyGrowth", self.context.get("response").keys())

    except requests.exceptions.RequestException:
        print("API request limit reached")
