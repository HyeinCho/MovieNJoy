<template>
  <div>
      <template v-if="review">
          <!-- 리뷰 페이지로 이동 -->
          <router-link :to="{ name: 'TicketDetailPage', 
            params: { id: review.id } }" class="text-decoration-none">        
          <TicketReviewItem :ticketReview="review" :movie="movie"/>
          </router-link>
      </template>
      <template v-else-if="movie">
          <!-- 영화 정보 페이지로 이동 -->
          <router-link :to="{ name: 'MovieDetailPage', 
          params: { id: movie.movie_pk } }" 
          class="text-decoration-none">  
          <TicketPosterItem :movie="movie" class="w-100"/>
          </router-link>
      </template>
  </div>
</template>

<script>
import TicketPosterItem from './TicketPosterItem.vue'
import TicketReviewItem from './TicketReviewItem.vue'
export default {
  components: { TicketPosterItem, TicketReviewItem },
    name:"TicketDiscoveryItem",
    props:{
        movie : Object,
        review : Object,
    }
}
</script>

<style>

</style>