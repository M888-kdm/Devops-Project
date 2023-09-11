from django.test import TestCase,Client
from django.urls import reverse
from .models import Utilisateur

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
    def setUp(self):
        self.client = Client()

    def test_get_visit_count(self):
        # Perform a GET request to the 'get_visit_count' view
        url = reverse('formulaire:visit_count')
        response = self.client.get(url)

        # Check if the view returns an HTTP 200 response
        self.assertEqual(response.status_code, 200)

        # Check if the 'visit_count_users' and 'visit_count_index' variables increment correctly
        initial_users_count = response.context['visit_count_users']
        initial_index_count = response.context['visit_count_index']

        # Access the 'user_list' URL (not 'users')
        user_list_url = reverse('formulaire:user_list')
        self.client.get(user_list_url)

        # Access the '' (empty) URL
        empty_url = reverse('formulaire:index')
        self.client.get(empty_url)

        # Perform another GET request to the 'get_visit_count' view
        response = self.client.get(url)

        # Verify that 'visit_count_users' and 'visit_count_index' have incremented by 1
        self.assertEqual(response.context['visit_count_users'], initial_users_count + 1)
        self.assertEqual(response.context['visit_count_index'], initial_index_count + 1)
