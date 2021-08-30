<template>
  <div class="discovery-view">
    <div class="discovery-box">
    <div class="discovery">
    <!-- <h1>This is an discovery page</h1> -->
    <div class="row">
      <div v-for="(ticket, idx) in tickets" :key="idx" class="col-3">

        <template v-if="ticket===0">
          <!-- 포스터 티켓 -->
          <TicketDiscoveryItem :movie="movie" style="height:95%;"/>
        </template>
        <template v-else>
          <!-- 리뷰 티켓 -->
          <TicketDiscoveryItem :review="ticket" :movie="movie" />
        </template> 
      </div>
    </div>
    <!-- <TicketBothList :tickets="tickets"/> -->
    </div>
    </div>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { getDiscovery, loadMovieData } from '@/api/index'
import _ from 'lodash'
// import TicketBothList from '../components/reviews/TicketBothList.vue'
import TicketDiscoveryItem from '../components/reviews/TicketDiscoveryItem.vue'
export default {
  name: 'DiscoveryPage',
  components: { 
    // TicketBothList, 
    TicketDiscoveryItem },
  data:function(){
    return{
      tickets : [],
      movie : null,
    }
  },
  // 2. created: async 함수의 형태로 axios 요청에 대한 답변 처리
  created: async function(){
      try{
      
        // axios 요청으로 랜덤한 리뷰 데이터를 받아온다.
        const { data } = await getDiscovery()

        // 영화 포스터 주소 얻어오기
        this.movie = await this.loadMovie(data[0].movie_pk)

        // 리뷰들 값 설정
        let reviews = data
        // 총 티켓 장 수
        const ALL_TICKET_NUM = 26
        this.tickets = Array.from({length: ALL_TICKET_NUM}, () => 0);
        let random_num = _.sampleSize( _.range(ALL_TICKET_NUM), reviews.length)
        for(let r of random_num){
            // 리뷰 티켓
            if(reviews.length>0){
              let review = reviews.pop()
              this.tickets[r] = review
            }
        }
        console.log(this.tickets)
      }catch (error) {
        console.log(error.response)
      } 
  },
  methods:{
    loadMovie: async function(movie_id){
      try{    
        // // axios 요청으로 데이터를 받아온다.
        const { data } = await loadMovieData(movie_id)      
        return data
      }catch (error) {
        console.log(error.response)
      } 
    }, 
  }
}
</script>

<style scoped>
.discovery-view{
  overflow-x: hidden;
  overflow-y:hidden;
}
.discovery-box{
   width: 100vw;
   height: 91vh;
   overflow: hidden;
   position: relative;
}
.discovery{
  z-index: -2;
  transform: translate(-5%, -15%) rotate(45deg); /* Equal to rotateZ(45deg) */
  /* background-color: pink; */
  /* position: absolute;
  overflow: visible; */
}
body {
  overflow: hidden;
}

</style>