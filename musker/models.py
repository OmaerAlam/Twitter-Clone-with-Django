from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Meep model
class Meep(models.Model):
    user = models.ForeignKey(
        User, related_name="meeps", 
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True)

    # Keep track of likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} ({self.created_at:%Y-%m-%d %H:%M}): {self.body}..."

# User Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    
    # Corrected the date_modified field
    data_modified = models.DateTimeField(User, auto_now=True)
    
    # Profile Image
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    # Bio and Links
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    homepage_link = models.CharField(null=True, blank=True, max_length=100)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)
    instagram_link = models.CharField(null=True, blank=True, max_length=100) 
    linkedin_link = models.CharField(null=True, blank=True, max_length=100)
    
    def __str__(self):
        return self.user.username

# Create Profile when new User signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

# Connecting the signal to create Profile after a User is saved
post_save.connect(create_profile, sender=User)
