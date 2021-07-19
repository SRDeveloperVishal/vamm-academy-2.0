from django.db import models
import datetime

# Create your models here.
class jobs(models.Model):
    title = models.CharField(max_length=255 , blank=True)
    job_details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    link = models.TextField(blank=True)
    job_link = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'jobs'

# class Test(models.Model):
#     title = models.CharField(max_length=255 , blank=True)

#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name_plural = 'Test'
