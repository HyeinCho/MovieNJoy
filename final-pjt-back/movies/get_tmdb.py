import requests, json

class URLMaker():
    base_url = 'https://api.themoviedb.org/3'
    
    # 생성자
    def __init__(self, key):
        self.key = key

    # url 반환 
    def get_url(self, category, feature, **kwargs):
        url = f'{self.base_url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        # 가변인자로 받아온 값을 쿼리스트링 방식으로 url에 이어준다.
        for key, value in kwargs.items():
            url += f'&{key}={value}'

        return url


def make_genre(movies):
    data = []
    for idx, movie in enumerate(movies['genres']):
        movie_data = {'model': 'movies.genre', 'pk': idx+1, 'fields': {}}
        for i in ['id', 'name']:
            movie_data['fields'][i] = movie[i]
        data.append(movie_data)
    
    with open('movies/fixtures/movies/genres.json', 'w', encoding='utf-8') as make_file:
        json.dump(data, make_file, indent="\t")


# def make_movie(movies):
#     data = []
#     for idx, movie in enumerate(movies['genres']):
#         movie_data = {'model': 'movies.genre', 'pk': idx+1, 'fields': {}}
#         for i in ['title', 'subtitle', 'overview', 'tagline', 'backdrop', 'release_date']:
#             movie_data['fields'][i] = movie[i]
#         movie_data['fields']['id'] = idx + 1
#         movie_data['fields']['movie_pk'] = movie['id']
#         movie_data['fields']['thumbnail'] = movie['poster_path']
#         movie_data['fields']['userRating'] = round(movie['vote_average'] / 2, 1)

#         for genre in response['genres']:
#             tmp = Genre.objects.filter(pk=genre['id'])
#             movie.genres.add(tmp[0])
#         data.append(movie_data)
    
#     with open('movies/fixtures/movies/movies.json', 'w', encoding='utf-8') as make_file:
#         json.dump(data, make_file, indent="\t")


# maker = URLMaker("")
# url = maker.get_url('genre', 'movie/list', language='ko')
# response = requests.get(url).json()
# make_genre(response)

# def get_json():
#     movie_list = []
#     # json파일을 db에 작성하려면 형식을 잘 갖춰야함
#     # model키에 appname.modelname 형식으로 들어가야하며
#     # 나머지 항목들은 fields키에 딕셔너리형태로 작성되어야 함
#     for movie_info in movies_raw_info:
#         movie = {}
#         movie['model'] = 'movies.movie'
#         fields = {}
#         fields['title'] = movie_info['title']
#         fields['overview'] = movie_info['overview']
#         fields['release_date'] = movie_info['release_date']
#         fields['poster_path'] = movie_info['poster_path']
#         movie['fields'] = fields
#         movie_list.append(movie)
        
#     file = open('movie_data.json', 'w', encoding='utf-8')
#     # encoding은 한글이 깨지지 않도록 하는 역할
#     file.write(json.dumps(movie_list, ensure_ascii = False, indent = '\t'))
#     # ensure_ascii는 한글이 깨지지 않도록 하는 역할, indent는 자동 indent를 해주는 역할
#     file.close


# maker = URLMaker("718613323d994402eeccde79f2f2a426")
# url = maker.get_url('movies', 'popular', language='ko')
# response = requests.get(url).json()
# make_genre(response)

# open("movies.json","wb").write(open("movie.json").read().decode("unicode_escape").encode("utf8")) 

# import codecs 
# src = "movie.json" 
# dst = "movies.json" 
# source = codecs.open(src, 'r').read().decode('utf-8') 
# codecs.open(dst, "wb").write(source) 