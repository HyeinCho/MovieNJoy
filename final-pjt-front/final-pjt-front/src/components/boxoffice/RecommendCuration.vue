<template>
  <div class="row">
      <div class="col-md-9 col-12 d-flex flex-column align-items-center">
          <p class="speech-bubble w-100"> {{ recommend_keyword }} 장르의 영화를 추천해드릴까요? </p>
          <div>
          <transition name="fade">
          <MovieGenreList :movies="recommend_movies" />
          </transition>
          </div>
          <button class="btn btn-outline-secondary w-50 my-4"
          @click="loadNewRecommend"
          >
               다른 영화를 추천해주실 수 있나요? 
            </button>
      </div>
      <div class="col-md-3">
          <img height="400" src="https://2.bp.blogspot.com/-VguKXW7Xa3U/VpjA_mpID7I/AAAAAAAA23M/0TveNN9UNhs/s800/kaden_tenin11_woman.png"/>
      </div>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { recommendGenre } from '@/api/index'
import MovieGenreList from '../movies/MovieGenreList.vue'

export default {
  components: { MovieGenreList },
    name:"RecommendCuration",
    data:function(){
        return{
            recommend_keyword:'',
            recommend_movies: [],
        }
    },
    // 2. created: async 함수의 형태로 axios 요청에 대한 답변 처리
    created: async function(){
        this.loadNewRecommend()
    },
    methods : {
        async loadNewRecommend(){
            try{
                // axios 요청으로 데이터를 받아온다.
                const { data } = await recommendGenre()
                this.recommend_keyword = data.genre_name
                this.recommend_movies = data.movieList

            }catch (error) {
                console.log(error.response)
            } 
        }

    }
}
</script>

<style scoped>
.speech-bubble {
	position: relative;
	background: #f0f0f0;
	border-radius: .4em;
    color: #000;
    padding: 1rem;
}

.speech-bubble:after {
	content: '';
	position: absolute;
	right: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 0.625em solid transparent;
	border-left-color: #f0f0f0;
	border-right: 0;
	border-top: 0;
	margin-top: -0.312em;
	margin-right: -0.625em;
}
</style>