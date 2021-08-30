<template>
  <div class="container">
      <div class="row">
        <div class=
        "offset-xxl-3 col-xxl-6 
          offset-lg-2 col-lg-8 
          offset-sm-1 col-sm-10
          col-12">
        <!-- 돌아가기 버튼 -->
        <div class="d-flex">
          <button @click="goBack" class="btn btn-sm btn-outline-secondary my-3">
              <i class="fas fa-arrow-left"></i> 돌아가기
          </button>
        </div>

      <template v-if="movie">
          <div class="row">
            <div class="d-sm-none d-md-block col-md-6">
            <TicketPosterItem :movie="movie" class="col-6"/>
            </div>
          <!-- 티켓 에디터 -->
          <TicketReviewEditor :movie="movie" class="col-md-6 col-12"/>
        </div>
      </template>
      </div>
    </div>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { loadMovieData } from '@/api/index'

import TicketReviewEditor from '../components/reviews/TicketReviewEditor.vue'
import TicketPosterItem from '../components/reviews/TicketPosterItem.vue'
export default {
  components: { TicketReviewEditor, TicketPosterItem },
    name:'TicketEditorPage',
    data: function(){
        return{
          movie: null,

        }
    },
    created:function(){
        // movie_id를 넘겨받았다면, 영화페이지에서 쓰러 가기
        if(this.$route.params.id != null){   
            this.movie_id = this.$route.params.id;
            this.loadMovie(this.movie_id)
        }
        
    },
    methods:{
        goBack(){
          this.$router.go(-1)
        },
        loadMovie : async function(movie_id){
            try{    
                // axios 요청으로 데이터를 받아온다.
                const { data } = await loadMovieData(movie_id)  
                this.movie = data
            }catch (error) {
                console.log(error.response)
            } 
        }
    }

}
</script>

<style>

</style>