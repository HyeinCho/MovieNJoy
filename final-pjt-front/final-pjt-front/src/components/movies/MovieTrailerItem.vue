<template>
  <div>
      <template v-if="video_id!=null && loaded">
        <transition name="fade" mode="out-in">
        <iframe id="ytplayer" type="text/html" width="640" height="360"
        :src="'https://www.youtube.com/embed/'+video_id+'?autoplay=1'"
        frameborder="0"></iframe>
        </transition>
        <!--autoplay not working : 크롬 보안 설정 때문에 자동재생 안 됨  -->
        <!-- <iframe id="ytplayer" type="text/html" width="640" height="360"
        :src="'https://www.youtube.com/embed/'+video_id+'?autoplay=1'"
        frameborder="0"></iframe> -->
      </template>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { loadMovieViedo } from '@/api/index'
export default {
    name:"MovieTrailerItem",
    props :{
        movie_id:Number,
    },
    data:function(){
        return {
            loaded : false,
            video_id: null,
        }
    },
    // 2. created: async 함수의 형태로 axios 요청에 대한 답변 처리
    created: async function(){
        try{
            // axios 요청으로 데이터를 받아온다.
            const { data } = await loadMovieViedo(this.movie_id)
            const video_url = data.youtube_url
            if(video_url!=''){
                this.video_id = video_url.split('=')[1]
            }
            this.loaded = true
        }catch (error) {
            console.log(error.response)
        } 
    },
}
</script>

<style>
/* fade 전환효과 */
.fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease-out; }
.fade-enter-from,.fade-leave-to { opacity: 0; }

/* slide-fade 전환효과 */
.slide-fade-enter { transform: translateX(10px); opacity: 0; } 
.slide-fade-enter-active, .slide-fade-leave-active { transition: all 0.2s ease; } 
.slide-fade-leave-to { transform: translateX(-10px); opacity: 0; }
</style>