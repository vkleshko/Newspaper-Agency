from django.core.exceptions import ValidationError
from django.test import TestCase

from newspaper_agency.forms import (
    RedactorCreationForm,
    RedactorSearchForm,
    NewspapersSearchForm,
    TopicSearchForm,
    validate_years_of_experience,
)


class RedactorCreationFormTests(TestCase):

    def test_redactor_creation_form_with_years_of_experience_first_last_name(self):
        form_data = {
            "username": "test123",
            "password1": "password123test",
            "password2": "password123test",
            "first_name": "user_test",
            "last_name": "test_user",
            "years_of_experience": 10
        }
        form = RedactorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, form_data)


class TopicSearchFormTests(TestCase):

    def test_blank_form(self):
        form_data = {}
        form = TopicSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_widgets_attributes(self):
        form = TopicSearchForm()

        self.assertIn('placeholder="Search by name"', str(form))


class RedactorSearchFormTests(TestCase):

    def test_blank_form(self):
        form_data = {}
        form = RedactorSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_widgets_attributes(self):
        form = RedactorSearchForm()

        self.assertIn('placeholder="Search by username"', str(form))


class NewspapersSearchFormTests(TestCase):

    def test_blank_form(self):
        form_data = {}
        form = NewspapersSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_widgets_attributes(self):
        form = NewspapersSearchForm()

        self.assertIn('placeholder="Search by title"', str(form))


class ValidateYearsOfExperienceTests(TestCase):

    def test_validation_error_when_years_of_experience_is_not_integer(self):
        with self.assertRaises(ValidationError):
            validate_years_of_experience("10")

    def test_validation_when_years_of_experience_not_in_range_0_100(self):
        with self.assertRaises(ValidationError):
            validate_years_of_experience(101)
