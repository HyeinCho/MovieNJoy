<template>
    <div class="row" data-masonry='{"percentPosition": true }'>
      <MovieItem v-for="(movie, idx) in movies" :key="idx" :movie="movie"
        class="col" />
    </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
export default {
    name:'MovieList',
    components: { 
        MovieItem 
    },
    props:{
        movies: Array,
    },
}
</script>

<style>

</style>