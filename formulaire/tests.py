from django.test import TestCase, Client
from django.urls import reverse
from .models import Utilisateur
from django.core.cache import cache

# Create your tests here.
class UserListViewTest(TestCase):
    def setUp(self):
        # Create sample user data for testing
        Utilisateur.objects.create(
            username="testuser",
            email="test@example.com",
            firstname="John",
            lastname="Doe",
        )

    def test_user_list_view(self):
        # Test if the user list view returns a 200 status code
        response = self.client.get(reverse("formulaire:user_list"))
        self.assertEqual(response.status_code, 200)

    def test_user_list_view_context(self):
        # Test if the user list view contains user data in the context
        response = self.client.get(reverse("formulaire:user_list"))
        users = response.context["users"]
        self.assertEqual(len(users), 1)  # Check if there is one user in the context

    def test_user_list_view_template(self):
        # Test if the user list view uses the correct template
        response = self.client.get(reverse("formulaire:user_list"))
        self.assertTemplateUsed(response, "formulaire/user_list.html")


# Unit test for visit_count
class GetVisitCountTestCase(TestCase):
    def test_get_visit_count_view(self):
        # Simulate a visit count in the cache
        cache.set('visits', 42)

        # Test if the get_visit_count view returns a 200 status code
        response = self.client.get(reverse("formulaire:visit_count"))
        self.assertEqual(response.status_code, 200)

    def test_get_visit_count_view_context(self):
        # Simulate no visits in the cache
        cache.delete('visits')

        # Test if the get_visit_count view contains visit count data in the context
        response = self.client.get(reverse("formulaire:visit_count"))
        visits = response.context["visits"]
        self.assertIsNone(visits)  # Check if visits context variable is None when no visits are cached

    def test_get_visit_count_view_template(self):
        # Simulate a visit count in the cache
        cache.set('visits', 42)

        # Test if the get_visit_count view uses the correct template
        response = self.client.get(reverse("formulaire:visit_count"))
        self.assertTemplateUsed(response, "formulaire/visit_count.html")
