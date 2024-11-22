from django.db import models
import uuid
# Create your models here.


class Auther(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.name} has {self.age} y/o'
    