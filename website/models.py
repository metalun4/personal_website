from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProfileInfo(models.Model):
    """
    author -> User
    profile_image
    profile_name
    bio
    resume
    location
    """
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=200)
    profile_name = models.CharField(max_length=50)
    show_email = models.BooleanField(default=False)
    bio = models.TextField()
    resume = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.profile_name


class SocialLinkInfo(models.Model):
    """
    name
    social_image
    """
    name = models.CharField(max_length=50)
    social_image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    """
    url
    social_info -> SocialLinksInfo
    belongs_to -> ProfileInfo
    """
    url = models.CharField(max_length=200)
    social_info = models.ForeignKey(SocialLinkInfo, on_delete=models.CASCADE)
    belongs_to = models.ForeignKey(ProfileInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class ProfileSkill(models.Model):
    """
    name
    belongs_to -> ProfileInfo
    """
    name = models.CharField(max_length=50)
    belongs_to = models.ForeignKey(ProfileInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
