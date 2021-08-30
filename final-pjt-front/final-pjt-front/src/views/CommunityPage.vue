<template>
  <div class="container">
    <!-- 타이틀 -->
    <h1 class="brand-font">Community</h1>
    <!-- 글 작성 버튼 -->
    <div class="d-flex justify-content-end">
      <router-link :to="{ name: 'PostCreatePage'}">
        <button class="btn btn-outline-secondary">Write New Post</button>
      </router-link>
    </div>
    
    <!-- 커뮤니티 리스트  -->
    <div>
      <CommunityList :posts=posts />
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

import CommunityList from '../components/community/CommunityList.vue'
// import TicketPosterItem from '../components/reviews/TicketPosterItem.vue'
// import TicketReviewList from '../components/reviews/TicketReviewList.vue'
export default {
  components: { 
    // TicketPosterItem, TicketReviewList, 
    CommunityList 
  },
    name: 'CommunityPage',
    computed:{
        ...mapGetters([
            'isLogin',
        ])
    },
    created : function(){
      // 로그인이 되지 않은 상태라면, 로그인 페이지로 이동
      if(!this.isLogin){
        this.$router.push({ name: 'Login' })
      }
    },
    data: function(){
      return {
        posts:null,
        ticketPoster:{
          path: "https://upload.wikimedia.org/wikipedia/ko/thumb/6/60/%EA%B8%B0%EC%83%9D%EC%B6%A9_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg/220px-%EA%B8%B0%EC%83%9D%EC%B6%A9_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
        },
        ticketReviews: [
          {
            title:"한국 영화 10년, 넘지 못할 선은 없다.",
            rating:"5",
          },
          {
            title:"한국 영화 10년, 넘지 못할 선은 없다.",
            rating:"5",
          },
          {
            title:"한국 영화 10년, 넘지 못할 선은 없다.",
            rating:"5",
          },
          {
            title:"한국 영화 10년, 넘지 못할 선은 없다.",
            rating:"5",
          }
        
        ]
      }
    }
}
</script>

<style>

</style>