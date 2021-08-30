from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('api-token-auth/', obtain_jwt_token),
    path('username/', views.username, name="username"),
    path('userinfo/', views.userinfo, name="userinfo"),
    path('isSignup/', views.isSignup, name="isSignup"),
    path('<str:username>/', views.profile, name="profile"),
    path('<str:username>/follow/', views.follow, name="follow"),
]
