from django.db import models

# Create your models here.
class Channel(models.Model): 
    channel_name = models.CharField(max_length=100) 
    description = models.TextField() 
    subscribers = models.PositiveIntegerField() 
    def __str__(self): 
        return self.channel_name
