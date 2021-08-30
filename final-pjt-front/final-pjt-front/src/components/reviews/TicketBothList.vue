<template>
    <div class="row">
        <div class="col-12 col-md-6 col-lg-4" v-for="(ticket, idx) in tickets" :key="idx">
         <router-link :to="{ name: 'TicketDetailPage', 
            params: { id: ticket.id } }" class="text-decoration-none"> 
            <TicketBothItem :ticket="ticket"/>
          </router-link>
        </div>
    </div>
</template>

<script>
import TicketBothItem from './TicketBothItem.vue'
export default {
    name:"TicketBothList",
    components: { TicketBothItem },
    props:{
        tickets:Array,
    }
}
</script>

<style>

</style>