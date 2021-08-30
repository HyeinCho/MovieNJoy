<template>
  <!--  comment.user  유저 이름으로 변경 필요 -->
  <div> 
    <p>
    <span class="badge bg-dark">{{ comment.username }}</span> {{ comment.comment }}
    <button type="button" @click="deleteComment" class="btn btn-sm btn-outline-secondary">x</button> 
    </p>
  </div>
</template>

<script>
import { commentDelete } from '@/api/index'

export default {
    name:"CommentItem",
    props:{
      comment:Object,
    }, 
    methods:{
      deleteComment : async function(event){
        event.preventDefault()
        try {
          // axios 요청으로 데이터를 보낸다
          await commentDelete(this.comment.article, this.comment.id)
          // 현재 리뷰 리스트 다시 로드하기
          // this.$emit('reloadComments')
          this.$router.go(this.$router.currentRoute)
        }
        catch(error) {
            console.log(error.response)
        }
      }
    }
}
</script>

<style>

</style>