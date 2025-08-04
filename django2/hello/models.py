from django.db import models
from django.utils import timezone
import datetime

class Greeting(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField("created at")

    def __str__(self):
        return self.text

    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


class Response(models.Model):
    greeting = models.ForeignKey(Greeting, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.response_text
