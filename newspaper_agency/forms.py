from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from newspaper_agency.models import Redactor, Newspaper, Topic


def validate_years_of_experience(years_of_experience):
    if not isinstance(years_of_experience, int):
        raise ValidationError(
            "Work experience should be integer number"
        )
    elif not (0 <= years_of_experience <= 100):
        raise ValidationError(
            f"Work experience should be in the range from 0 to 100, not {years_of_experience}"
        )
    return years_of_experience


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    years_of_experience = forms.IntegerField(
        label="Years of Experience",
        required=True,
        widget=forms.TextInput(attrs={'id': 'years_of_experience'}),
        validators=[validate_years_of_experience],
    )


class RedactorYearOfExperienceUpdateForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = ["years_of_experience"]

    years_of_experience = forms.IntegerField(
        label="Years of Experience",
        required=True,
        widget=forms.TextInput(attrs={'id': 'years_of_experience'}),
        validators=[validate_years_of_experience],
    )


class NewspapersSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )
