from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    title = RichTextField(max_length=255, blank=True) 
    pub_date = models.DateTimeField()
    # image = models.ImageField(upload_to='post_images/', blank=True)
    image = CloudinaryField("image", folder="blog_images/")
    body = RichTextField(blank=True)

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]
