from django.db import models
from django.utils.timezone import now 
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField

class Data(models.Model):
    MEDIUM=(
        ("bangla","bangla"),
        ("english","english"),
        ("german","german"),
        ("hindi","hindi"),
        ("arabi","arabi"),
        ("urdu","urdu"),
    )
    CATEGORY_CHOICES = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title=models.CharField(max_length=100,default='a title')
    slug=models.CharField(max_length=100,default='title')
    age = models.IntegerField(default=0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES,default="Teacher")
    image = models.ImageField(default='default.jpg', upload_to='firstapp/images')
    medium=MultiSelectField(max_length=100,max_choices=5,choices=MEDIUM,default="bangla")
    
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Data,self).save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.width>300 or img.height>300:
            output=(300,300)
            img.thumbnail(output)
            img.save(self.img.path)
            
        

    def __str__(self):
        return self.name
