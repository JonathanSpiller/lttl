from django.db import models

from datetime import datetime

class Url(models.Model):

    original = models.CharField(max_length=500)
    little = models.CharField(max_length=20)
    created = models.DateTimeField(default=datetime.now, blank=True)
    
    def __repr__(self):
        return f"URL - Original: {self.original[:20]}, little: {self.little}"

    def __str__(self):
        return f"URL - Original: {self.original[:20]}, little: {self.little}"

