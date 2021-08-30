<template>
  <div>
      <div class="movie-item">
      <template v-if="movie != null">
        <router-link :to="{ name: 'MovieDetailPage', params: { id: movie.id } }"
        class="text-decoration-none">
            <!-- 영화 이미지가 DB에 존재하지 않을 경우, 플레이스 홀더 표시 -->
            <template v-if="movie.poster_path===null">
               <img class="poster-placeholder" src="https://via.placeholder.com/300/000000/FFFFFF/?text=No+Poster+Image" alt="movie_poster"/>
            </template>
            <!-- 존재할 경우 포스터 이미지 표시 -->
            <template v-else>
            <img :src="'https://image.tmdb.org/t/p/w300/'+movie.poster_path" 
            alt="movie_poster" class="movie-poster"/>
            </template>
            <h2 v-text="movie.title" class="mb-0 nav-link text-white"></h2>
            <p v-text="movie.release_date" class="text-white-50"></p>  
        </router-link>
      </template>
      </div>
  </div>
</template>

<script>
export default {
    name:'MovieItem',
    props : {
        movie: Object,
    },

    methods :{
  
    },
}
</script>

<style scoped>
.poster-placeholder{
    width:300px;
    height: 450px;
    object-fit: contain;
}
    li{
        list-style-type: none;
    }
    img{
        border: 4px white solid;
    }
    .movie-item:hover > img{
        filter: brightness(150%);
        -webkit-filter: brightness(150%);
    }
    img:hover{
        filter: brightness(150%);
        -webkit-filter: brightness(150%);
    }
    h2{
        font-size: 1rem;
    }
    p{
        font-size: 0.8rem;
        display: inline;
    }
</style>