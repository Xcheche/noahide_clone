from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    # image = models.ImageField(default="default.jpg",upload_to='images/', blank=True)
    # image = CloudinaryField("image", folder="blog_user_images/",default="default.jpg")
    image = CloudinaryField("image", folder="blog_user_images/",default="https://res.cloudinary.com/df6ndrlj2/image/upload/v1739969127/default_sklyca.png",
                            transformation={"width": 300, "height": 300, "crop": "fill"})
    
    
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
 
    # Resizing image automatically
    # def save(self, *args, **kwargs):
    #     # Call the parent save method with all arguments
    #     super().save(*args, **kwargs)

    #     # Resize the image
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         if img.height > 300 or img.width > 300:
    #             output_size = (300, 300)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
   