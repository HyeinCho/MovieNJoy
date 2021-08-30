<template>
    <div class="container">
        <div class=
        "offset-xxl-3 col-xxl-6 
          offset-lg-2 col-lg-8 
          offset-sm-1 col-sm-10
          col-12">
            <!-- 돌아가기 버튼 -->
            <div class="d-flex justify-content-between">
            <button @click="goBack" class="btn btn-sm btn-outline-secondary my-3">
                <i class="fas fa-arrow-left"></i> 돌아가기
            </button>
            <h4><i class="ms-2 fa-heart" :class=" [heart ? 'fas' : 'far', heart_animate ? 'animate__animated animate__tada' : ' '] "
                 @click="ToggleHeart"></i> {{ heart_count }} </h4>
            <!-- 작성자의 정보와 일치할 때만, 삭제 버튼 출력 -->
            <template v-if="this.ticket">
            <div v-if="username==this.ticket.username">
                <button @click="deleteReview" class="btn btn-sm btn-outline-secondary my-3">
                    <i class="fas fa-trash-alt"></i> 삭제
                </button>
            </div>
            </template>
            </div>
          
            <TicketBothItem v-if="ticket!=null" :ticket="ticket"/>
        </div>
    </div>
</template>

<script>
// 1. api/index.js의 axios 요청 함수들
import { reviewDetail, reviewDelete, reviewLike } from '@/api/index'
import { mapState, mapGetters } from 'vuex'
import TicketBothItem from '../components/reviews/TicketBothItem.vue'
export default {
  components: { TicketBothItem },
    name:"TicketDetailPage",
    computed:{
      ...mapState([
          'username', // 좋아요 여부 확인을 위한 유저이름
      ]),
    ...mapGetters([
        'isLogin',
    ])
    },
    created: async function(){
        try{
            //   넘겨준 리뷰 Pk 기준으로
            this.review_id = this.$route.params.id;

            // axios 요청으로 데이터를 받아온다.
            const { data } = await reviewDetail(this.review_id)
            this.ticket = data

            // 로그인 되어있다면,
            if ( this.isLogin ){
                // API 좋아요 요청
                try {
                    // axios 요청으로 데이터를 보낸다
                    const res = await reviewLike(this.review_id, {'user': this.username, 'flag': false})
                    this.changeHeartIcon(res.data)
                }
                catch(error) {
                    console.log(error.response)
                }
            }
      }catch (error) {
        console.log(error.response)

      } 
    },
    data: function(){
        return {
            // 리뷰 티켓 정보
            review_id : null,
            ticket : null,

            // 사용자의 좋아요 여부 변수
            heart:false,
            // 페이지 로드 때 하트 애니메이션 자동 재생 되는 것 막고,
            // 유저가 새로 클릭 했을 때만 애니메이션 발생시키기 위해서 분리한 변수
            heart_animate:true,
            heart_count: 0,
        }
    },
    methods:{
        // 뒤로가기
        goBack(){
          this.$router.go(-1)
        },
        // 리뷰 삭제
        async deleteReview(){
            await reviewDelete(this.review_id)
            // 티켓박스 페이지로 이동
            this.$router.push({ name: 'TicketboxPage'});
        },
        // 리뷰 좋아요
        changeHeartIcon : function(isHeart){
            this.heart_count = isHeart.likeCnt
            this.heart = isHeart.liked
            if(this.heart){
                this.heart_animate = true
            }else{
                this.heart_animate = false
            }
        },
        ToggleHeart: async function(){
            // 로그인 되어있지 않다면,
            if ( !this.isLogin ){  
                // 로그인 페이지로 리다이렉트
                this.$router.push({ name: 'Login' }) 
            }else{
                // API 좋아요 요청
                try {
                    // axios 요청으로 데이터를 보낸다
                    const res = await reviewLike(this.review_id, {'user': this.username, 'flag': true})
                    this.changeHeartIcon(res.data)
                }
                catch(error) {
                    console.log(error.response)
                }
                
                // 현재 리뷰 리스트 다시 로드하기
                // this.$emit('reloadComments')
                // this.$router.go(this.$router.currentRoute)
            }
        }
    }
}
</script>

<style>

</style>