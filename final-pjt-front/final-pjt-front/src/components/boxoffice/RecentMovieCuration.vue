<template>
  <div>
      <p class="mt-2">NOW SHOWING</p>
      <MovieCarouselList :movies="movies" class="flex-nowrap"/>
  </div>
</template>

<script>
import { nowMovies } from '@/api/index'
import MovieCarouselList from '../movies/MovieCarouselList.vue'
export default {
    name: 'RecentMovieCuration',
    components: { 
        MovieCarouselList 
    },
    data: function(){
        return {
            movies : null,
        }
    },
    created: async function(){
      try{
        // api/index.js 에 있는 axios 함수 호출. 
        // url은 파일에 지정되어 있음.
        const { data } = await nowMovies()

        // 갱신할 데이터
        this.movies = data.data

      }catch (error) {
        console.log(error.response)
      } 
    }
}
</script>

<style>

</style>