from typing import Reversible
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Article, Comment
from accounts.models import User
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    articles = Article.objects.all().order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET': # 반환
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 1. 해당 article의 유저가 아닌 경우 todo를 수정하거나 삭제하지 못하게 설정
    if not request.user.article_set.filter(pk=article_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT': # 수정
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE': # 삭제
        article.delete()
        data = {
            '{}번 리뷰가 삭제되었습니다'.format(article_pk)
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_create(request, article_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, article_id=article_pk)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        article = get_object_or_404(Article, id=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_detail(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user != comment.user:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT': # 수정
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE': # 삭제
        comment.delete()
        data = {
            '{}번 리뷰가 삭제되었습니다'.format(comment_pk)
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # 로그인 한 유저 정보
    username = request.data['user']
    user = User.objects.get(username=username)

    # 맨 처음 로드했을 때
    if not request.data['flag']:
        if article.like_users.filter(pk=user.pk).exists():
            liked = True
        else:
            liked = False

        like_status = {
            'liked': liked,
            'likeCnt': article.like_users.count()          
        }
        return JsonResponse(like_status)
    
    # 클릭했을 때
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True
        
    like_status = {
        'liked': liked,
        'likeCnt': article.like_users.count()          
    }
    return JsonResponse(like_status)
