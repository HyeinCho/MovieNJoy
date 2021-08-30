<template>
  <div>
    <template v-if="movie!=null">
    <!-- 영화관 디자인 틀 -->
    <div class="d-flex align-items-stretch mb-2">
      <div class="curtain"></div>
        <!-- 영화정보 -->
        <MovieInfo :movie="movie" class="movie-info"/>
      <div class="curtain"></div>
    </div>
    <!-- 영화 태그라인 -->
    <template v-if="movie.tagline!=null && movie.tagline!=''">
    <div class="contents my-5 w-75">
        <blockquote> <h2>{{ movie.tagline }}</h2> </blockquote>
    </div>
    </template>
    <!-- 영화 트레일러 -->
    <div class="contents my-5">
      <MovieTrailerItem :movie_id="movie.movie_pk"/>
    </div>
    <!-- 영화 리뷰 -->
    <div class="contents">
      <h3 class="title mb-3">Best Reviews</h3>
      <template v-if="reviews === null || reviews.length === 0">
        <h5 class="mb-2" v-text="no_review"></h5>
        <!-- 새 리뷰티켓 만들기 -->
        <router-link 
        :to="{ name: 'TicketCreateFromMoviePage', 
        params: { id: movie.movie_pk }}">
          <button class="btn btn-sm btn-outline-secondary">'{{ movie.title }}'의 리뷰 티켓 만들기 <i class="fas fa-edit"></i></button>
        </router-link>
        <!-- 새 리뷰 티켓 만들기 끝 -->
      </template>
      <div v-else>
        <TicketReviewList :ticketReviews="reviews" :movie="movie"/>
      </div>
    </div>
    <!-- 비슷한 영화 -->
    <template v-if="similar_movies!=null && similar_movies.length!=0">
    <div class="contents">
        <h3 class="title mb-3"> '{{ movie.title }}' 비슷한 영화 </h3>
        <MovieCarouselList :movies="similar_movies"/>
    </div>
    </template>
    
    <!-- 이 영화를 본 사람들이 본 다른 영화 -->
    <template v-if="audiences!=null && audiences.length!=0">
    <div class="contents">
      <h3 class="title mb-3">'{{ movie.title }}' 본 사람들은 어떤 영화를 봤을까?</h3>
      <AudienceList :audiences="audiences" />
    </div>
    </template>
    </template>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { loadMovieData, loadMovieBestReviews, recommendSimilar, recommendAnother } from '@/api/index'
import AudienceList from '../components/movies/AudienceList.vue'
import MovieInfo from '../components/movies/MovieInfo.vue'
import TicketReviewList from '../components/reviews/TicketReviewList.vue'
import MovieTrailerItem from '../components/movies/MovieTrailerItem.vue'
import MovieCarouselList from '../components/movies/MovieCarouselList.vue'
export default {
  name: 'MovieDetailPage',
  components: { 
    MovieInfo,
    AudienceList,
    TicketReviewList,
    MovieTrailerItem,
    MovieCarouselList 
  },
  // 2. created: async 함수의 형태로 axios 요청에 대한 답변 처리
  created: async function(){
      try{
        //   넘겨준 영화 Pk 기준으로
        const movie_id = this.$route.params.id;
        
        // axios 요청으로 데이터를 받아온다.
        const { data } = await loadMovieData(movie_id)
        this.movie = data
        this.loadBestReviews(movie_id)
        this.loadSimilarMovies(movie_id)
        this.recommendAnother(movie_id)
      }catch (error) {
        console.log(error.response)
      } 
  },
  methods : {
    async loadBestReviews(movie_id){
        try{
          // axios 요청으로 데이터를 받아온다.
          const { data } = await loadMovieBestReviews(movie_id)
          this.reviews = data.reviews
        }catch (error) {
          console.log(error.response)
        } 
    },
    async loadSimilarMovies(movie_id){
      try{
          // axios 요청으로 데이터를 받아온다.
          const { data } = await recommendSimilar(movie_id)
          this.similar_movies = data.movieList
        }catch (error) {
          console.log(error.response)
        } 
      
    },
    async recommendAnother(movie_id){
        try{
          // axios 요청으로 데이터를 받아온다.
          const { data } = await recommendAnother(movie_id)
          this.audiences = data.movies
        }catch (error) {
          console.log(error.response)
        } 
    }
  },
  data: function(){
    return {
      no_review: '아직 영화를 본 사람이 없어요',
      movie:null,
      audiences:[],
      reviews : null,
      similar_movies: null,
    }
  }
}
</script>

<style scoped>
.curtain{
  display: float;
  width: 10%;
  height: auto;
  background-image: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(255,255,255,0) 15%, rgba(255,255,255,0) 85%, rgba(0,0,0,1) 100%), url('../assets/red_curtain.jpg') ;
  background-repeat: repeat;
  background-size: auto 120%;
}
.contents{
  width: 80%;
  margin: 0% 10%;
}

.title{
  margin-top:3rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid white;
}

blockquote:before {
  content: "\201C";
  font-size: 3em;
  font-family: Georgia;
  color: #bcbcbc;
  float: left;
  margin: -5px 10px 0px -10px;
}

</style>