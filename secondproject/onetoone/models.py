from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    
    
    def __str__(self):
        return f"{self.name} the place"
class Restaurant(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE)  
    # here place bring from Place class or place table by using onetoone relation 
    serves_hot_dogs=models.BooleanField(default=False)
    serves_pizze=models.BooleanField(default=False)
    
    def __str__(self):
        return "%s the restaurant" % self.place.name 


class Waiter(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    
    name=models.CharField(max_length=50)
    def __str__(self):
        return "%s the waiter at %s "%(self.name,self.restaurant)
    