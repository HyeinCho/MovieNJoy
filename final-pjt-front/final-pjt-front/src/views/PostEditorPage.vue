<template>
    <div class="container">   
        <h1 class="brand-font">Post Editor</h1>
        <PostEditor :id="id"/>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PostEditor from '../components/community/PostEditor.vue'
export default {
  components: { PostEditor },
    name:"PostEditorPage",
    data:function(){
        return {
            id : null,
        }
    },    
    computed:{
        ...mapGetters([
            'isLogin',
        ])
    },
    created:function(){
      // 로그인이 되지 않은 상태라면, 로그인 페이지로 이동
      if(!this.isLogin){
        this.$router.push({ name: 'Login' })
      }

      // 수정이어서 넘어온 값이 있다면, 이전 포스트의 내용 불러오기
        if(this.$route.params.id){
            this.id = Number(this.$route.params.id)
        }
    }
}
</script>

<style>

</style>