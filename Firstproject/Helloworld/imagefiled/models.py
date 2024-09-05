from django.db import models
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField

class ImageDescription(models.Model):
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
    slug = models.CharField(max_length=100, unique=True, blank=True)
    image = models.ImageField(default='defaults.jpg', upload_to='images/')
    medium=MultiSelectField(default='bangla',max_length=100,max_choices=5,choices=MEDIUM)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug from title
        if not self.slug:
            self.slug = slugify(self.title)
        super(ImageDescription, self).save(*args, **kwargs)

        # Resize the image if necessary
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
