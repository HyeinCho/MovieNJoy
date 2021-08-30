<template>
<div class="container">
  <template v-if="profile!=null">
  <div class="row">
    <div class="col-12 col-sm-4 col-md-3">
      <!-- 프로필 이미지 및 유저 이름 -->
      <AudienceItem :audience="profile"/>
    </div>
    <div class="col-12 col-sm-8 col-md-9">
      <!-- 유저 정보 -->
      <UserInfo :user="profile"/>
      <template v-if="profile!==null">
        <MovieList :ticket="profile.favoriteMovie"/>
      </template>
    </div>
  </div>
  <div>
    <Headline :title="profile_name+'님이 좋아하는 영화'"/>
    <movie-list :movies="favorite_movies"/>
    <TicketPosterList :ticketPosters="favorite_movies"/>
  </div>
  <div>
    <Headline :title="profile_name+'님의 리뷰 티켓'"/>
    <TicketBothList :tickets="my_reviews"/>
  </div>
  </template>
</div>
</template>

<script>
import { getProfile, userMoviesList, userReviewsList } from '@/api/index'
// import FavoriteMovie from '../components/accounts/FavoriteMovie.vue'
import UserInfo from '../components/accounts/UserInfo.vue'
import Headline from '../components/Headline.vue'
import AudienceItem from '../components/movies/AudienceItem.vue'
import TicketPosterList from '../components/reviews/TicketPosterList.vue'
import TicketBothList from '../components/reviews/TicketBothList.vue'
import { mapState } from 'vuex'
import MovieList from '../components/movies/MovieList.vue'

export default {
  components: { AudienceItem, UserInfo, 
  // FavoriteMovie, 
  Headline, TicketBothList, TicketPosterList,
    MovieList },
  name: 'Profile',
  computed: {
    ...mapState([
      'user',
    ])
  },
  created: function(){
    // username 라우터에서 받아옴
    this.profile_name = this.$route.params.username
    if(this.profile_name){
      this.loadProfile()
      this.loadFavoriteMovie()
      this.loadMyReviews()
    }
  },
  methods: {
    loadProfile : async function(){
       try{
        const { data } = await getProfile(this.profile_name)
        this.profile =  data

      }catch (error) {
        console.log(error.response)
      } 
    },
    loadFavoriteMovie : async function(){
       try{
        const { data } = await userMoviesList(this.profile_name)

        for (let movie of data){
          // thumbnail, movie_pk를 poster_path, id로 사용한다
          movie['poster_path'] = movie.thumbnail
          movie['id'] = movie.movie_pk
          this.favorite_movies.push(movie)
        }
        // this.favorite_movies = data
      }catch (error) {
        console.log(error.response)
      } 
    },
    loadMyReviews: async function(){
       try{
        const { data } = await userReviewsList(this.profile_name)
        this.my_reviews = data
      }catch (error) {
        console.log(error.response)
      } 
    },
    
  },
  data:function(){
    return{
      profile_name:null,
      profile: null,
      favorite_movies :[],
      my_reviews: [],
    }
  }
}
</script>

<style>

</style>