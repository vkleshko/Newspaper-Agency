from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from newspaper_agency.forms import TopicSearchForm

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


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "newspaper_agency/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["topic_search"] = TopicSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TopicCreatedView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper_agency:topic-list")
