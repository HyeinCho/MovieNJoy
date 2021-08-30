<template>
    <div>
        <Headline :title="title"/>
        <TicketBothItem :ticketPoster="ticket.poster" :ticketReview="ticket.review"/>
    </div>
</template>

<script>
import Headline from '../Headline.vue'
import TicketBothItem from '../reviews/TicketBothItem.vue'
export default {
    name:"FavoriteMovie",
    components: { TicketBothItem, Headline },
    data : function(){
        return {
            title:"당신의 Favorite Movie",
        }
    },
    props:{
        ticket:Object,
    },
    computed:{
        // title:"님의 Favorite Movie"
    }
}
</script>

<style>

</style>