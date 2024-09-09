from django.db import models
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.utils.timezone import now

class Imagedescription(models.Model):
    MEDIUM_CHOICES = (
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('french', 'French'),
        ('hindi', 'Hindi'),
        ('german', 'German'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=101)
    slug = models.CharField(max_length=100, editable=False)  # Change default=True to editable=False
    image = models.ImageField(default='default.jpg', upload_to='images/')
    available = models.BooleanField()
    details = models.TextField()
    created_at = models.DateTimeField(default=now)
    
    # Adding the MEDIUM field as a MultiSelectField
    medium = MultiSelectField(choices=MEDIUM_CHOICES, max_choices=3, max_length=15)  # Adjust max_choices and max_length as needed

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Imagedescription, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # Fix reference to self.image.path

