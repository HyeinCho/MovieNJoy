<template>
  <div class="movie-info container" 
  :style="{ 'background-image': 'url(https://image.tmdb.org/t/p/original' + movie.backdrop + ')' }">
      <div class="row movie-content-holder">
        <div class="movie-content col-12 col-sm-8 col-md-9 order-2 order-sm-1">
            <!-- 영화 타이틀 -->
            <div class="title-holder d-flex align-items-center mt-5">
                <h1>{{ movie.title }}</h1>
                <!-- 좋아요 버튼 -->
                <h4><i class="ms-2 fa-heart" :class=" [heart ? 'fas' : 'far', heart_animate ? 'animate__animated animate__tada' : ' '] "
                 @click="ToggleHeart"></i> </h4>
            </div>
            <!-- 영화 타이틀 끝 -->
            <!-- 별점 | 개봉일 | 장르 -->
            <h6><i class="fas fa-star"></i> {{ movie.userRating }} |  
                {{ movie.release_date }} |
                <span v-for="(genre,idx) in movie.genres" :key=idx 
                  v-text="'#'+genre.name" class="mx-1"></span>
            </h6>
            <!-- 줄거리 -->
            <p class="my-3">{{ movie.overview }}</p>
            
        </div>
        <div class="col-12 col-sm-4 col-md-3 order-1 order-sm-2">
        <!-- 영화 포스터 이미지 -->
            <!-- 영화 이미지가 DB에 존재하지 않을 경우, 플레이스 홀더 표시 -->
            <template v-if="movie.thumbnail===null">
                <div my-3>

                </div>
            </template>
            <!-- 존재할 경우 포스터 이미지 표시 -->
            <template v-else>
                <img class="movie-poster my-2" 
                :src="'https://image.tmdb.org/t/p/original'
                +movie.thumbnail" />
            </template>
        <!-- 리뷰 티켓 만들기 버튼 -->
            <router-link 
                :to="{ name: 'TicketCreateFromMoviePage', 
                params: { id: movie.movie_pk }}">
            <button class="btn btn-sm btn-outline-secondary my-3">리뷰 티켓 만들기 <i class="fas fa-edit"></i></button>
            </router-link>
        </div>
    </div>
  </div>
</template>

<script>
import { movieLike } from '@/api/index'
import { mapState, mapGetters } from 'vuex'
export default {
    name:"MovieInfo.vue",
    props:{
        movie: null,
    },
    data:function(){
        return{
            loaded: false,
            // 사용자의 좋아요 여부 변수
            heart:false, // 기본은 false
            // 페이지 로드 때 하트 애니메이션 자동 재생 되는 것 막고,
            // 유저가 새로 클릭 했을 때만 애니메이션 발생시키기 위해서 분리한 변수
            heart_animate:false,
        }
    },
    computed:{
        ...mapState([
            'username', // 좋아요 여부 확인을 위한 유저이름
        ]),
        ...mapGetters([
            'isLogin',
        ])
    },
    created : async function(){
        // 로그인 되어있다면,
        if ( this.isLogin ){
            // API 좋아요 요청
            try {
                // axios 요청으로 데이터를 보낸다
                const res = await movieLike(this.movie.movie_pk, {'user': this.username, 'flag': false})
                if (res.data.liked) {
                    this.heart = true
                }else{
                    this.heart = false
                }
                this.loaded = true
            }
            catch(error) {
                console.log(error.response)
            }
            
            // 현재 리뷰 리스트 다시 로드하기
            // this.$emit('reloadComments')
            // this.$router.go(this.$router.currentRoute)
        }
    },
    methods:{
        changeHeartIcon : function(isHeart){
            this.heart = isHeart
            if(this.heart){
                this.heart_animate = true
            }else{
                this.heart_animate = false
            }
        },
        ToggleHeart: async function(){
            // 로그인 되어있지 않다면,
            if ( !this.isLogin ){  
                // 로그인 페이지로 리다이렉트
                this.$router.push({ name: 'Login' }) 
            }else{
                // API 좋아요 요청
                try {
                    // axios 요청으로 데이터를 보낸다
                    const res = await movieLike(this.movie.movie_pk, {'user': this.username, 'flag': true})
                    this.changeHeartIcon(res.data.liked)
                }
                catch(error) {
                    console.log(error.response)
                }
                
                // 현재 리뷰 리스트 다시 로드하기
                // this.$emit('reloadComments')
                // this.$router.go(this.$router.currentRoute)
            }
        }
    }
}
</script>

<style scoped>
.movie-info {
    width: 90%;
    background-size: cover;
}
.movie-content{
    padding: 0 5%;
    z-index: 1;

}
.movie-content-holder {
    backdrop-filter: brightness(25%);
}
h1, h6, p {
    text-align: left;
}
.fa-heart.fas {
    color:red;
}
.background {
  position: fixed;
  left: 0;
  right: 0;
  display: block;
  
  width: 1200px;
  height: 800px;
  background-size: cover;
  background-repeat: no-repeat;
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(5px);
}
.movie-poster{
    filter: drop-shadow(0 0 0.75rem grey);
}
img{
    width: 100%;
}

.poster-placeholder{
    width:300px;
    height: 450px;
    object-fit: contain;
}
</style>