from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('discovery/', views.discovery, name="discovery"),
    path('genre_recommend/', views.genre_recommend, name="genre_recommend"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
    path('<str:q>/', views.movie_list, name="movie_list"),
    path('search/<str:keyword>/', views.search, name="search"),
    path('<int:movie_pk>/video/', views.movie_video, name="movie_video"),
    path('<int:movie_pk>/review/', views.review_create, name="review_create"),
    path('review/<int:review_pk>/', views.review_detail, name="review_detail"),
    path('reviews/<int:movie_pk>/', views.movie_reviews, name="movie_reviews"),
    path('<int:movie_pk>/likes/', views.movie_like, name="movie_like"),
    path('review/<int:review_pk>/likes/', views.review_like, name="review_like"),
    path('<int:movie_pk>/best_review/', views.best_review, name="best_review"),
    path('<int:movie_pk>/another_movie/', views.another_movie, name="another_movie"),
    path('<int:movie_pk>/similar_movie/', views.similar_movie, name="similar_movie"),
    path('<str:username>/user_reviews_list/', views.user_reviews_list, name="user_reviews_list"),
    path('<str:username>/user_movies_list/', views.user_movies_list, name="user_movies_list"),
]
