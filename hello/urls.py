from django.urls import path
from . import views

urlpatterns = [
    path("", views.greeting_list, name="greeting_list"),
    path("greeting/<int:greeting_id>/", views.greeting_detail, name="greeting_detail"),
]
