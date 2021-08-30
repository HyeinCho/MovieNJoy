<template>
   <ul class="row" v-if="ticketReview!=null">
    <li class="col-12 col-sm-6">
      <TicketPosterItem :movie="movie"/>
    </li>
    <li class="col-12 col-sm-6">
      <TicketReviewItem :ticketReview="ticketReview" :movie="movie"/>
    </li>
  </ul>

</template>

<script>
import { loadMovieData } from '@/api/index'
import TicketPosterItem from './TicketPosterItem.vue'
import TicketReviewItem from './TicketReviewItem.vue'
export default {
    name:'TicketBothItem.vue',
    components: { TicketPosterItem, TicketReviewItem },
    props: {
      ticket:Object,
    },
    data :function(){
      return{
        movie: null,
        ticketPoster : null,
        ticketReview : null,
      }
    },
    created : async function(){
      try{
        const movie_id = this.ticket.movie_pk // 영화 ID
        
        // // axios 요청으로 데이터를 받아온다.
        const { data } = await loadMovieData(movie_id)
        this.movie = data           
        this.ticketReview = this.ticket
      }catch (error) {
        console.log(error.response)
      } 
    }, 

}
</script>

<style scoped>
li{
  list-style-type: none;
}
</style>