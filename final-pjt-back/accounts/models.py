from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    profile_img = models.ImageField(upload_to="profile/", default="media/profile/basic.png")
    introduce = models.CharField(max_length=50, default="영화뉴비")
    favorite_movie = models.IntegerField(blank=True, null=True) # id 저장

    def __str__(self):
        return f'{self.pk} - {self.username}'
        