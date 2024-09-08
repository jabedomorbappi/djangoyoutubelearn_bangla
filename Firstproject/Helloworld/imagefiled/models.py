from django.db import models
from django.db import models
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
# Create your models here.
from django.utils.timezone import now


class Imagedescription(models.Model):
    MEDIUM=(
        ('bangla','bangla'),
        ('english','english'),
        ('french','french'),
        ('Hhindi','hindi'),
        ('german','german'),
        )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=101)
    slug = models.CharField(max_length=100, default=True)
    image = models.ImageField(default='defaults.jpg', upload_to='images/')
    available=models.BooleanField()
    details=models.TextField()
    created_at=models.DateTimeField(default=now)
    image=models.ImageField(default='default.jpg',upload_to='images/')
    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Imagedescription,self).save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.img.path)
            
        
