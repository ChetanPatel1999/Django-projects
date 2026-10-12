from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subscribers_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name
