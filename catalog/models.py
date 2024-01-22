from django.db import models
from django.urls import reverse

# Create your models here.

class Searches(models.Model):
    term = models.CharField(max_length=100)
    location = models.CharField(max_length=100)



#for testing purposes
class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()


class Business(models.Model):
    """Model representing a business"""

    name = models.CharField(max_length=200)
    biz_id = models.CharField(max_length = 250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the url of a detail page for this business"""
        return reverse('biz', args=[str(self.id)])