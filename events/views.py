from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
# Create your views here.


def event_detail_view(request, id):
    obj = get_object_or_404(Event, id=id)
    context = {
        "object": obj
    }
    return render(request, "event_detail.html", context)


def event_list_view(request):
    queryset = Event.objects.all()
    context = {
        'events': queryset
    }
    return render(request, "event.html", context)
