from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper_agency.admin import NewspaperAdmin
from newspaper_agency.models import Newspaper, Topic


class RedactorAdminTests(TestCase):

    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin1234",
            years_of_experience=10
        )
        self.client.force_login(self.admin_user)

        self.redactor = get_user_model().objects.create_user(
            username="adminds",
            password="admin12sd34",
            years_of_experience=10
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:newspaper_agency_redactor_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_detail_years_of_experience_listed(self):
        url = reverse("admin:newspaper_agency_redactor_change", args=[self.redactor.id])
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)


class NewspaperAdminTest(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin1234",
            years_of_experience=10
        )
        self.client.force_login(self.admin_user)

        self.site = AdminSite()
        self.newspaper_admin = NewspaperAdmin(Newspaper, self.site)

        self.topic = Topic.objects.create(name="tests")

        self.newspaper = Newspaper.objects.create(
            title="tests",
            context="tests context",
            topic=self.topic,
        )

    def test_list_display(self):
        self.assertIn("title", self.newspaper_admin.list_display)
        self.assertIn("context", self.newspaper_admin.list_display)
        self.assertIn("topic", self.newspaper_admin.list_display)

    def test_list_filter(self):
        self.assertIn("topic__name", self.newspaper_admin.list_filter)

    def test_search_fields(self):
        self.assertIn("title", self.newspaper_admin.search_fields)

    def test_newspaper_display(self):
        url = reverse("admin:newspaper_agency_newspaper_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tests")

    def test_search_newspaper(self):
        url = reverse("admin:newspaper_agency_newspaper_changelist")
        response = self.client.get(url, {'q': 'Test Newspaper'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tests")
