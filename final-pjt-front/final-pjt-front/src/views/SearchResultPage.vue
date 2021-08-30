<template>
  <div>
      <h1>#<span v-text="keyword" class="mb-3"> </span> </h1>
      <div class="search-result">
      <!-- 검색결과가 있는 경우 -->
      <template v-if="movies">
        <MovieList :movies="movies" />
      </template>
      <!-- 검색결과가 없는 경우, 최신 영화 추천 -->
      <template v-else>
          <h3> 검색 결과가 없습니다. <br/> 최근에 개봉한 다른 영화들을 둘러보는 건 어떠신가요? </h3>
          <RecentMovieCuration/>
      </template>
      </div>  
  </div>
</template>

<script>
import { searchMovies } from '@/api/index'
import MovieList from '../components/movies/MovieList.vue'
import RecentMovieCuration from '../components/boxoffice/RecentMovieCuration.vue'
export default {
    components: { MovieList, RecentMovieCuration },
    name:"SearchResultPage",
    data: function(){
        return {
            keyword: '',
            movies : null,
        }
    },
    created: function(){
      //   넘겨준 검색 키워드 기준으로  
      this.keyword = this.$route.params.keyword
      this.search()
    },
    methods:{
        async search(){
            try{
                // api/index.js 에 있는 axios 함수 호출. 
                // url은 파일에 지정되어 있음.
                const { data } = await searchMovies(this.keyword)

                // 갱신할 데이터
                if (data.results.length != 0)
                    this.movies = data.results

            }catch (error) {
                console.log(error.response)
            } 
        }
    }

}
</script>

<style>

</style>