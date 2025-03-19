from django.db import models
from django_countries.fields import CountryField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    location = CountryField()

    def __str__(self):
        return self.name
class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'