from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey is a link to another model
    title = models.CharField(max_length=200) # CharField is for text with a limited number of characters
    text = models.TextField() # TextField is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now) # DateTimeField is for date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() # timezone.now() is a function that returns the current time
        self.save()

    def __str__(self):
        return self.title