from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Favorite


# Create your tests here.
class FavoriteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        Favorite.objects.create(name="apple", user=self.user)

class test_api(TestCase):
    def checkVol(self):
        response = self.client.get('/search_results/')
        self.assertIn('quoteResponse', response.json())

    def checkCap(self):
        response = self.client.get('/search_results/')
        self.assertIn('quoteResponse', response.json())

    def checkEarnings(self):
        response = self.client.get('/search_results/')
        self.assertIn('quoteSummary', response.json())

    def test_animals_can_speak(self):
        apple_fav = Favorite.objects.get(user=self.user, name="apple")
        self.assertEqual(apple_fav.user.username, "testuser")
        self.assertEqual(apple_fav.name, "apple")
