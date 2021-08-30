<template>
  <div class="w-100">
      <form class="btn-group d-grid gap-2" role="group" >
          <input type="text" v-model="data.comment" 
          class=""
          name="contents" id="contents" @keydown.enter="submit">
          <button class="btn btn-sm btn-outline-secondary" 
          @click="submit">write</button>
      </form>
  </div>
</template>

<script>
import { commentCreate } from '@/api/index'

export default {
    name:"CommentEditor",
    props:{
        pk : Number,
    },
    data:function(){
        return{
            data :{
                comment:'',
            }
        }
    },
    methods:{
        // !!!!!!!!!다영님 참고!!!!!!!!!!!!
        // 아까 db 뭐 할 때 contents로 안돼서 comment로 바꿨어요
        // 뭔가 Article에 있는 contents랑 겹쳐서 그런건가/... 아님 걍 운 안좋게 실행이 갑자기 안돼서 그런건가...
        // 그래서 Comment에 있는 내용은 comment 변수로 진행됩니다!!
        // 이 페이지는 바꿔나서 잘 구동돼요!!
        submit:async function(event){
            event.preventDefault()
            this.$emit('reloadComments')
            try {
                // axios 요청으로 데이터를 보낸다
                await commentCreate(this.pk, this.data)
                // 코멘트 입력 후 입력창 초기화
                this.data = {
                    comment:'',
                }

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