from django.contrib import admin
from .models import Greeting, Response

class ResponseInline(admin.TabularInline): 
    model = Response
    extra = 1  

class GreetingAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at", "was_created_recently")
    inlines = [ResponseInline]  
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("greeting", "response_text", "votes")

admin.site.register(Greeting, GreetingAdmin)
admin.site.register(Response, ResponseAdmin)
