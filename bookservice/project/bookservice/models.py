from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=30)
    author_id = models.CharField(max_length=36)  # Store UUID as string
    price = models.DecimalField(decimal_places=2,max_digits=8)
    
    def __str__(self):
        return self.name
    