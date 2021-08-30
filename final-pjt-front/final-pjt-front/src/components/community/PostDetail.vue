<template>
  <div>
      <!-- 글 제목 -->
      <h1 class="title" v-text="post.title">Title</h1>
      <h4><i class="ms-2 fa-heart" :class=" [heart ? 'fas' : 'far', heart_animate ? 'animate__animated animate__tada' : ' '] "
                 @click="ToggleHeart"></i> {{ heart_count }} </h4>
      <!-- 글 작성자 -->
      <router-link :to="{ name: 'ProfilePage', params: { username: post.username } }" >    
        <p class="author link-light" v-text="post.username"></p>
      </router-link>
      <!-- 글 작성시간 -->
      <p class="created-at" > {{ post.created_at | timeDisplay }} </p>
      <!-- 글 내용 -->
      <p class="content" v-text="post.content"> </p>          
  </div>
</template>

<script>
import { articleLike } from '@/api/index'
import { mapState, mapGetters } from 'vuex'
export default {
    name:"PostDetail",
    props:{
        post:Object,
    },
    data:function(){
        return{
            // 사용자의 좋아요 여부 변수
            heart:false,
            // 페이지 로드 때 하트 애니메이션 자동 재생 되는 것 막고,
            // 유저가 새로 클릭 했을 때만 애니메이션 발생시키기 위해서 분리한 변수
            heart_animate:false,
            heart_count: 0,
        }
    },
    computed:{
        ...mapState([
            'username', // 좋아요 여부 확인을 위한 유저이름
        ]),
        ...mapGetters([
            'isLogin',
        ])
    },
    created : async function(){
        // 로그인 되어있다면,
        if ( this.isLogin ){
            // API 좋아요 요청
            try {
                // axios 요청으로 데이터를 보낸다
                const res = await articleLike(this.post.id, {'user': this.username, 'flag': false})
                this.heart_count = res.data.likeCnt
                if (res.data.liked) {
                    this.heart = true
                }else{
                    this.heart = false
                }
            }
            catch(error) {
                console.log(error.response)
            }

        // this.heart = this.post.like_users.includes(this.username)
        
        // 현재 리뷰 리스트 다시 로드하기
        // this.$emit('reloadComments')
        // this.$router.go(this.$router.currentRoute)
        }
        
    },
    methods:{
        changeHeartIcon : function(isHeart){
            this.heart = isHeart
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
                    const res = await articleLike(this.post.id, {'user': this.username, 'flag': true})
                    this.heart_count = res.data.likeCnt
                     this.changeHeartIcon(res.data.liked)

                    // 페이지 내 좋아요 아이콘 변경
                    // if (this.heart){
                        
                    // }else{
                        
                    // }
                }
                catch(error) {
                    console.log(error.response)
                }
                
                }
        }
    },
    filters:{
      // 날짜 표현방식 직관적으로
      timeDisplay: function (createdAt){
        const milliSeconds = new Date() - Date.parse(createdAt)
        const seconds = milliSeconds / 1000
        if (seconds < 60) return `방금 전`
        const minutes = seconds / 60
        if (minutes < 60) return `${Math.floor(minutes)}분 전`
        const hours = minutes / 60
        if (hours < 24) return `${Math.floor(hours)}시간 전`
        const days = hours / 24
        if (days < 7) return `${Math.floor(days)}일 전`
        const weeks = days / 7
        if (weeks < 5) return `${Math.floor(weeks)}주 전`
        const months = days / 30
        if (months < 12) return `${Math.floor(months)}개월 전`
        const years = days / 365
        return `${Math.floor(years)}년 전`
      }
    }


}
</script>

<style scoped>
.content{
    min-height: 80%;
}

</style>