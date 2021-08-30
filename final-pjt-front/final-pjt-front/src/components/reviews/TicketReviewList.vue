<template>
  <div class="row">
      <div class="col-3" v-for="(ticketReview, idx) in ticketReviews" 
      :key="idx">
      <router-link :to="{ name: 'TicketDetailPage', 
            params: { id: ticketReview.id } }" class="text-decoration-none">        
          <TicketReviewItem :ticketReview="ticketReview" :movie="movie"/>
      </router-link>
      </div>
  </div>
</template>

<script>
import TicketReviewItem from './TicketReviewItem.vue'
export default {
  components: { TicketReviewItem },
    name:'TickeReviewList',
    props : {
        ticketReviews:Array,
        movie:Object,
    },
    created: function(){
    }
}
</script>

<style>

</style>