from django.db import models

# Create your models here.

class YouTubeCoreses(models.Model):
    title = models.CharField(max_length=255)
    course_details = models.TextField()
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
