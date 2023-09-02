from django.test import TestCase,Client
from django.urls import reverse
from .models import Utilisateur
from .views import visit_count

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


class VisitCountTestCase(TestCase):
    def test_visit_count(self):
        # Create a new client to simulate HTTP requests
        client = Client()

        # Send a GET request to the visit_count endpoint
        response = client.get(reverse('formulaire:visit_count'))

        # Check that the response contains the correct count
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This website has been visited', response.content)