from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper_agency.models import Topic, Newspaper, Redactor


def index(request):
    topics = Topic.objects.count()
    newspapers = Newspaper.objects.count()
    redactors = Redactor.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topics": topics,
        "num_newspapers": newspapers,
        "num_redactors": redactors,
        "num_visits": num_visits + 1,
    }

    return render(request, "newspaper_agency/index.html", context=context)
