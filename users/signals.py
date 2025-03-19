from django.conf import settings
from django.contrib.auth.models import User
#from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create the profile
        Profile.objects.create(user=instance)
        
        # Send an email
        # send_mail(
        #     subject='Welcome to My Cheche\'s Blog!',
        #     message=f'Hi {instance.username}, your profile has been created successfully! Feel free to edit your profile.',
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[instance.email],
        #     fail_silently=False,
        # )

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()