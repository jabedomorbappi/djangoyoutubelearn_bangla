from django.db import models

class Data(models.Model):
    CATEGORY_CHOICES = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default="Teacher")
    image = models.ImageField(default='default.jpg', upload_to='firstapp/images')

    def __str__(self):
        return self.name
