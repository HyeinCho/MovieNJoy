<template>
    <div class="row">
      <MovieItem v-for="(movie, idx) in movies" :key="idx" :movie="movie"
        class="col" />
    </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
export default {
    name:'MovieGenreList',
    components: { 
        MovieItem 
    },
    props:{
        movies: Array,
    },
}
</script>

<style scoped>
/* 자식 요소에게만 스타일 적용 /deep/ */
/deep/ .movie-poster{
    width:150px;
}
</style>