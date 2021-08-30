from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import UserSerializer, UserProfileSerializer
from .models import User

@api_view(['POST'])
def signup(request):
    # client에서 데이터를 받음
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    # 패스워드 일치 여부 확인
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱
        user.set_password(request.data.get('password'))
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def username(request):
    user = get_object_or_404(User, pk=request.user.pk)
    context = {
        'username': user.username
    }
    return JsonResponse(context)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def userinfo(request):
    user = get_object_or_404(User, pk=request.user.pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data) 


@api_view(['POST'])
def isSignup(request):
    user = User.objects.filter(username=request.user.username)
    if user:
        return JsonResponse({isSignup: True})
    else:
        return JsonResponse({isSignup: False})


@api_view(['POST'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data) 


@api_view(['POST'])
def follow(request, username):
    # 어차피 이거 로그인 안되어 있으면 위에 데코에 걸려서 로그인으로 가든지 할듯
    # 유저가 로그인되어있지 않으면
    # if not request.user.is_authenticated:
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    profile_user = get_object_or_404(User, username=username)
    login_user = get_object_or_404(User, username=request.data['login_user']
)
    if not request.data['flag']:
        # 팔로우인 경우
        if profile_user.followers.filter(pk=login_user.pk).exists():
            followed = True
        # 언팔인 경우
        else:
            followed = False
    else:
        # 본인과 유저가 다른 경우
        if login_user != profile_user:
            # 팔로우인 경우 => 언팔로우
            if profile_user.followers.filter(pk=login_user.pk).exists():
                profile_user.followers.remove(login_user)
                followed = False
            # 언팔인 경우 => 팔로우
            else:
                profile_user.followers.add(login_user)
                followed = True
        
    follow_status = {
        'followed': followed,
        'following': profile_user.followings.count(),
        'follower': profile_user.followers.count(),
    }

    return JsonResponse(follow_status)
