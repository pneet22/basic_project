from django.shortcuts import render, get_object_or_404
from .models import Greeting, Response

def greeting_list(request):
    greetings = Greeting.objects.all()
    return render(request, "greetings/greeting_list.html", {"greetings": greetings})

def greeting_detail(request, greeting_id):
    greeting = get_object_or_404(Greeting, pk=greeting_id)
    responses = Response.objects.filter(greeting=greeting)
    return render(request, "greetings/greeting_details.html", {
        "greeting": greeting,
        "responses": responses
    })