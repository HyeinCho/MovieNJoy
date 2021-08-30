<template>
    <div class="container">
      <h1>Movies</h1>
      <MovieList :movies="movies" />
    </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D" crossorigin="anonymous" async></script>
<script>

import { loadMovies } from '@/api/index'
import MovieList from '../components/movies/MovieList.vue'
export default {
  components: { MovieList },
  name:"MoviesPage",
  data: function(){
        return {
            movies : null,
        }
    },
    created: async function(){
      try{
        // api/index.js 에 있는 axios 함수 호출. 
        // url은 파일에 지정되어 있음.
        const { data } = await loadMovies()

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