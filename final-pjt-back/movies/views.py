from requests.api import get
from final_pjt_back.settings import TMDB_API, CLIENT_ID, CLIENT_SECRET
from .get_tmdb import URLMaker
from .models import Movie, Review, Genre, Director, Actor
from accounts.models import User
from .serializers import MovieSerializer, ReviewSerializer
import requests, json, urllib.request, random
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.db.models import Count, Q
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from pprint import pprint


def make_movie(movie_pk):
    maker = URLMaker(TMDB_API)
    # 영화 디테일
    url = maker.get_url('movie', movie_pk, region='KR', language='ko')
    response = requests.get(url).json()
    movie = Movie.objects.create()
    movie.movie_pk = movie_pk
    movie.title = response['title']
    movie.subtitle = response['original_title']
    movie.overview = response['overview']
    movie.tagline = response['tagline']
    movie.thumbnail = response['poster_path']
    movie.backdrop = response['backdrop_path']
    movie.release_date = response['release_date']
    movie.userRating = 0
    for genre in response['genres']:
        tmp = Genre.objects.filter(pk=genre['id'])
        movie.genres.add(tmp[0])
    
    # 영화 출연자, 감독 정보
    url = maker.get_url('movie', f'{movie_pk}/credits', language='ko')
    response = requests.get(url).json() 
    for crew in response['crew']:
        if crew['job'] == 'Director':
            if not Director.objects.filter(id=crew['id']):
                tmp = Director.objects.create(id=crew['id'], name=crew['name'])
            else:
                tmp = Director.objects.get(id=crew['id'])
            movie.directors.add(tmp)
    
    for cast in response['cast']:
        if not Actor.objects.filter(id=cast['id']):
            tmp = Actor.objects.create(id=cast['id'], name=cast['name'])
        else:
            tmp = Actor.objects.get(id=cast['id'])
        movie.actors.add(tmp)

    movie.save()


def update_rating(movie_pk):
    movie = get_object_or_404(Movie, movie_pk=movie_pk)
    reviews = Review.objects.filter(movie_id=movie.pk)
    if not reviews:
        maker = URLMaker(TMDB_API)
        url = maker.get_url('movie', movie_pk, region='KR', language='ko')
        response = requests.get(url).json() 
        movie.userRating = round(response['vote_average'] / 2)
    else:
        total = 0
        cnt = 0
        for review in reviews:
            total += review.rating
            cnt += 1
        movie.userRating = round(total / cnt, 1)
    movie.save()


def update_level(user_id):
    reviews = Review.objects.filter(user_id=user_id)
    user = User.objects.get(id=user_id)
    if len(reviews) <= 3:
        user.introduce = "영화 뉴비"
    elif len(reviews) <= 10:
        user.introduce = "영화 좀 볼 줄 아는 분인가?"
    elif len(reviews) <= 30:
        user.introduce = "혹시 꿈이 평론가?"
    else:
        user.introduce = "걸어다니는 영화위키피디아"
    user.save()


# now_playing: 현재 상영작
# popular: 인기순
@api_view(['GET'])
def movie_list(request, q):
    maker = URLMaker(TMDB_API)
    url = maker.get_url('movie', q, region='KR', language='ko')
    response = requests.get(url).json()
    # 전체 페이지 갯수 구함
    total_page = response['total_pages'] if response['total_pages'] <= 3 else 3
    
    context = {
        'data': []
    }

    # 해당 페이지에 있는 영화 정보들 넣기
    for page in range(1, total_page + 1):
        response = requests.get(url + f'&page={page}').json()
        context['data'].extend(response['results'])

    # 소트
    # context['data'].sort(key=lambda x:x['vote_average'], reverse=True)
    
    # serializer = json.dumps(context, indent=4)
    # return Response(serializer, status=status.HTTP_201_CREATED) 
    return JsonResponse(context)


@api_view(['GET'])
def movie_detail(request, movie_pk):    
    # db에 저장되어 있는 정보인 경우
    if len(Movie.objects.filter(movie_pk=movie_pk)) != 0:
        movie = get_object_or_404(Movie, movie_pk=movie_pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    # 그렇지 않은 경우
    else:
        maker = URLMaker(TMDB_API)
        url = maker.get_url('movie', movie_pk, region='KR', language='ko')
        response = requests.get(url).json() 

        # genre
        genres = []
        for genre in response['genres']:
            genres.append({'id':genre['id'], 'name':genre['name']})

        # 영화 출연자, 감독 정보
        url = maker.get_url('movie', f'{movie_pk}/credits', language='ko')
        response1 = requests.get(url).json() 
        
        directors = []
        for crew in response1['crew']:
            if crew['job'] == 'Director':
                directors.append({'id':crew['id'], 'name':crew['name']})
        
        actors = []
        for cast in response1['cast']:
            actors.append({'id':cast['id'], 'name':cast['name']})

        context = {
            "review_set": [],
            "movie_pk": movie_pk,
            "title": response['title'],
            "subtitle": response['original_title'],
            "overview": response['overview'],
            "tagline": response['tagline'],
            "thumbnail": response['poster_path'],
            "backdrop": response['backdrop_path'],
            "release_date": response['release_date'],
            "userRating": round(response['vote_average'] / 2),
            "directors": directors,
            "actors": actors,
            "genres": genres,
            "like_users": [],
        }

        return Response(context)


def search(request, keyword):
    maker = URLMaker(TMDB_API)

    # 영화 검색
    url = maker.get_url('search', 'movie', query=keyword, region='KR', language='ko')
    response = requests.get(url).json() 
    
    # 영화 검색 결과가 없으면 인물 검색
    if not response['results']:
        url = maker.get_url('search', 'person', query=keyword, region='KR', language='ko')
        response = requests.get(url).json()

    return JsonResponse(response)
    

def movie_video(request, movie_pk):
    maker = URLMaker(TMDB_API)
    url = maker.get_url('movie', f'{movie_pk}/videos', language='ko')
    response = requests.get(url).json() 
    if len(response['results']) == 0:
        return JsonResponse({'youtube_url': ''})
    else:
        youtube_key = response['results'][0]['key']
        youtube_url = f'https://www.youtube.com/watch?v={youtube_key}'
        return JsonResponse({'youtube_url': youtube_url})


# 리뷰 쓰기
# 로그인 된 채로 잘 되느냐!!! 체크
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    # 해당 영화 정보가 없을 때
    # 영화를 db에 저장
    if not len(Movie.objects.all()) or not Movie.objects.filter(movie_pk=movie_pk):
        make_movie(movie_pk)
        
    movie = get_object_or_404(Movie, movie_pk=movie_pk) 
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        update_rating(movie_pk)
        update_level(request.user.pk)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    movie = Movie.objects.get(id=review.movie_id)
    if request.method == 'GET': # 반환
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT': # 수정
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            update_rating(movie.movie_pk)
            update_level(request.user.pk)
            return Response(serializer.data)
    elif request.method == 'DELETE': # 삭제
        review.delete()
        data = {
            '{}번 리뷰가 삭제되었습니다'.format(review_pk)
        }
        update_rating(movie.movie_pk)
        update_level(request.user.pk)
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 특정 영화의 모든 리뷰 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_reviews(request, movie_pk):
    movie = get_object_or_404(Movie, movie_pk=movie_pk)
    reviews = get_list_or_404(Review, movie_id=movie.pk)
    Review.objects.filter(movie_id=movie.pk).order_by('-thumb_users')

    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 특정 유저의 모든 리뷰 조회
@api_view(['POST'])
def user_reviews_list(request, username):
    # username = request.data['username']
    user = User.objects.get(username=username)
    reviews = get_list_or_404(Review, user_id=user.pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# 특정 유저가 좋아하는 모든 영화 조회
@api_view(['POST'])
def user_movies_list(request, username):
    user = User.objects.get(username=username)
    movies = Movie.objects.filter(like_users=user.pk)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 좋아요
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):    
    # 해당 영화 정보가 없을 때
    # 영화를 db에 저장
    if len(Movie.objects.all()) == 0 or len(Movie.objects.filter(movie_pk=movie_pk)) == 0:
        make_movie(movie_pk)
        update_rating(movie_pk)
    
    movie = get_object_or_404(Movie, movie_pk=movie_pk)
    # 로그인 한 유저 정보
    username = request.data['user']
    user = User.objects.get(username=username)

    # 맨 처음 로드했을 때
    if not request.data['flag']:
        if movie.like_users.filter(pk=user.pk).exists():
            liked = True
        else:
            liked = False

        like_status = {
            'liked': liked,
            'likeCnt': movie.like_users.count()          
        }
        return JsonResponse(like_status)
        
    # 클릭 했을 때
    if movie.like_users.filter(id=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True

    like_status = {
        'liked': liked,
        'likeCnt': movie.like_users.count()          
    }
    return JsonResponse(like_status)


# 리뷰 좋아요
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = Review.objects.filter(pk=review_pk)
    # review = get_object_or_404(Review, pk=review_pk)
    if len(review) == 0:
        like_status = {
            'liked': False,
            'likeCnt': 0         
        }
        return JsonResponse(like_status)

    # 로그인 한 유저 정보
    username = request.data['user']
    user = User.objects.get(username=username)
    review = review[0]

    # 맨 처음 로드했을 때
    if not request.data['flag']:
        if review.thumb_users.filter(pk=user.pk).exists():
            liked = True
        else:
            liked = False
    else:
        if review.thumb_users.filter(pk=user.pk).exists():
            review.thumb_users.remove(user)
            liked = False
        else:
            review.thumb_users.add(user)
            liked = True
    
    like_status = {
        'liked': liked,
        'likeCnt': review.thumb_users.count()          
    }
    return JsonResponse(like_status)


def best_review(request, movie_pk):
    movie = Movie.objects.filter(movie_pk=movie_pk)
    context = { 'reviews': [] }
    if len(movie) == 0:
        return JsonResponse(context)

    reviews = Review.objects.filter(movie_id=movie[0].id).annotate(num_thumbs=Count('thumb_users')).order_by('-num_thumbs')
    if len(reviews) > 4:
        reviews = reviews[:4]
    for review in reviews:
        context['reviews'].append(
            {
                'user': review.user_id,
                'movie_pk': movie[0].movie_pk,
                'id': review.pk,
                'rating': review.rating,
                'content': review.content,
                'created_at': review.created_at
            }
        )
    return JsonResponse(context)


@api_view(['GET'])
def discovery(request):
    while True:
        movie = Movie.objects.all().order_by('?')[0]
        reviews = Review.objects.all().filter(movie_id=movie.pk)
        if reviews:
            for review in reviews:
                if not review.rating:
                    break
            else:
                serializer = ReviewSerializer(reviews, many=True)
                break
    return Response(serializer.data)


# 해당 영화를 본 사람들이
# 다른 영화를 뭘 봤는지
# review가 기준
def another_movie(request, movie_pk):
    movie = Movie.objects.filter(movie_pk=movie_pk)
    context = { 'movies': [] }
    if not movie:
        return JsonResponse(context) 
    # movie = get_object_or_404(Movie, movie_pk=movie_pk)
    # print(movie.id)
    user_list = []
    while len(user_list) < 4 and len(user_list) < len(Review.objects.filter(movie_id=movie[0].pk)):
        user = Review.objects.all().filter(movie_id=movie[0].pk).order_by("?")[0]
        print(user)
        if user in user_list:
            continue
        user_list.append(user)

    for user_one in user_list:
        review = Review.objects.all().filter(Q(user_id=user_one.user_id) and ~Q(movie_id=movie[0].id)).order_by("?")[0]
        if not review:
            continue
        tmp = Movie.objects.get(id=review.movie_id)
        context['movies'].append(
            {
                'movie_pk': tmp.movie_pk,
                'title': tmp.title,
                'user': user_one.user_id,
                'username': review.user.username,
            }
        )
    return JsonResponse(context)


# 장르 추천 시스템
def genre_recommend(request):

    maker = URLMaker(TMDB_API)
    url = maker.get_url('movie', 'popular', region='KR', language='ko')
    response = requests.get(url).json()
    # 전체 페이지 갯수 구함
    total_page = 5

    while True:
        movie_list = []
        genre = Genre.objects.all().order_by('?')[0]
        for page in range(1, total_page + 1):
            response = requests.get(url + f'&page={page}').json()
            for data in response['results']:
                if genre.id in data['genre_ids']:
                    tmp = {
                        'id': data['id'],
                        'title': data['title'],
                        'poster_path': data['poster_path'],
                        'release_date': data['release_date']
                    }
                    movie_list.append(tmp)

        if len(movie_list) >= 4:
            break

    movie_status = {
        'movieList': random.sample(movie_list, 4),
        'genre_name': genre.name,
    }


    # for movie in movies:
    #     tmp = {
    #         'pk': movie.movie_pk,
    #         'title': movie.title,
    #         'thumbnail': movie.thumbnail,
    #         'release_date': movie.release_date,
    #     }
    #     movieList.append(tmp)
    # movie_status = {
    #     'movieList': movieList,
    #     'genre_name': genre.name,
    # }
    return JsonResponse(movie_status)


# 해당 영화와 비슷한 영화
def similar_movie(request, movie_pk):
    maker = URLMaker(TMDB_API)
    url = maker.get_url('movie', f'{movie_pk}/similar', language='ko')
    response = requests.get(url).json() 
    movieList = []
    for result in response['results']:
        movieList.append({
            'id': result['id'],
            'title': result['title'],
            'poster_path': result['poster_path'],
            'release_date': result['release_date'],
        })

    url = maker.get_url('movie', movie_pk, language='ko')
    response = requests.get(url).json() 

    movie_status = {
        'movieList': movieList,
        'movie_name': response['title']
    }
    return JsonResponse(movie_status)
