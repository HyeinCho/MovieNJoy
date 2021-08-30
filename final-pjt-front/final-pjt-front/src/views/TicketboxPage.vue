<template>
  <div class="container">
    <h1>TicketBox</h1>
    <!-- 티켓이 없을 때 -->
    <template v-if="tickets.length==0">
      <p class="mt-5 mb-2"> 잊지 못할 영화의 티켓에 리뷰를 남겨 간직해 보세요.</p>
      <router-link :to="{ name: 'MoviesPage'}">
          <button class="btn btn-sm btn-outline-secondary">첫 리뷰 티켓 만들기 <i class="fas fa-edit"></i></button>
      </router-link>
    </template>
    <!-- 티켓이 있을 때 -->
    <template v-else>
      <router-link :to="{ name: 'MoviesPage'}">
          <button class="btn btn-sm btn-outline-secondary mb-3">새 리뷰 티켓 만들기 <i class="fas fa-edit"></i></button>
      </router-link>
      <TicketBothList :tickets="tickets"/>
    </template>
  </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { userReviewsList } from '@/api/index'
import { mapState } from 'vuex'
import TicketBothList from '@/components/reviews/TicketBothList.vue'
export default {
  name: 'TicketboxPage',
  components: { TicketBothList },
  computed:{
      ...mapState([
          'username', // 좋아요 여부 확인을 위한 유저이름
      ])
  },
   // 2. created: async 함수의 형태로 axios 요청에 대한 답변 처리
  created: async function(){
      try{
        // axios 요청으로 데이터를 받아온다.
        const { data } = await userReviewsList(this.username)
        this.tickets = data

      }catch (error) {
        if (error.status==404){
          // this.noTicket = true
        }
        console.log(error.response)

      } 
  },
  data: function(){
    return {
      tickets : [],
    }
  }
}
</script>

<style>

</style>