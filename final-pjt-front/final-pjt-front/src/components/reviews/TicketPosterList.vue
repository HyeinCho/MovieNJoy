<template>
  <div class="row">
    <TicketPosterItem class="col-3" v-for="(ticketPoster,idx) in ticketPosters" :key="idx" :ticketPoster="ticketPoster"/>
  </div>
</template>

<script>
import TicketPosterItem from './TicketPosterItem.vue'
export default {
    name:'TicketPosterList',
    components: { TicketPosterItem },
    props:{
        ticketPosters:Array,
    }
}
</script>

<style>

</style>