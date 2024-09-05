from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    content=models.TextField(max_length=17)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    CATEGORY=(
        ('teacher','teacher'),
        ('student','student'),
    ) 
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    sluck=models.CharField(max_length=100,default=title)
    email=models.EmailField()
    salary=models.IntegerField()
    details=models.TextField()
    status=models.BooleanField()
    category=models.CharField(max_length=100,choices=CATEGORY)
    
    
    