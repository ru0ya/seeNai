from django.db import models


class Matwana(models.Model):
    name = models.CharField(max_length=20, unique=True)
    route = models.CharField(max_length=20)
    sacco = models.CharField(max_length=20)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class StreetFood(models.Model):
    name = models.CharField(max_length=20)
    average_price = models.IntegerField(default=0)
    ingredients = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class TouristDestination(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=20)
    open_days = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=20)
    average_price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
      