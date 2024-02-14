from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        ordering = ["username"]

    def get_absolute_url(self):
        return reverse("publisher_tracker:redactor-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(
        Topic,
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("publisher_tracker:newspaper-list")

    def __str__(self) -> str:
        return f"{self.title} {self.context} {self.topic}"
