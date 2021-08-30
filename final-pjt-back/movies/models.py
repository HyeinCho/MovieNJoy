from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk} - {self.name}'

class Director(models.Model):
    name = models.CharField(max_length=50)


class Actor(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    movie_pk = models.IntegerField(null=True) # 영화 pk
    title = models.CharField(max_length=500) # 영화 제목
    subtitle = models.CharField(max_length=500) # 영화 영문 제목
    overview = models.TextField() # 줄거리
    tagline = models.TextField() # 태그라인
    thumbnail = models.CharField(max_length=500) # 영화 썸네일 이미지 url
    backdrop = models.CharField(max_length=500) # 영화 배경 이미지 url
    release_date = models.DateField(null=True) # 영화 제작년월일
    userRating = models.FloatField(null=True) # 영화 평점
    directors = models.ManyToManyField(Director) # 영화 감독
    actors = models.ManyToManyField(Actor) # 영화 출연 배우
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies') # 좋아하는 사람


    def __str__(self):
        return f'{self.title} {self.directors}'


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    thumb_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='thumb_reviews', blank=True) # 좋아하는 사람


