from django.db import models

# Create your models here.
class Serials(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    genres = models.CharField(max_length=40)   
    info = models.CharField(max_length=1500) 
    
    #используем замечательный метод
    def __str__(self):
        return f'{self.pk}{self.name}'