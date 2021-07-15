from django.db import models
import datetime

# Create your models here.

class YouTubeCourses(models.Model):
    
    title = models.CharField(max_length=255 , blank=True)
    course_details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    link = models.TextField(blank=True)
    notes = models.FileField(upload_to='notes/', blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = 'YouTubeCourses'



