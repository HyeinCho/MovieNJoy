from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comment/', views.comments_create, name='comments_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comments_detail, name='comments_detail'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
