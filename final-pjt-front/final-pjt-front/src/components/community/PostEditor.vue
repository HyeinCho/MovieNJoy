<template>
  <div>
      <form class="d-flex flex-column">
          <input type="text" class="form-control my-1" v-model="data.title" placeholder="title">
          <textarea class="form-control my-1" rows="10" v-model="data.content" placeholder="content"> </textarea>
          <button class="my-1 btn btn-secondary" @click="submit">write</button>
      </form>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import { communityCreate, communityUpdate, communityDetail } from '@/api/index'
export default {
  name:"PostEditor",
  props :{
    id:Number,
  },
  data: function(){
    return {
      data : {
        title:'',
        content:''
      }
    }
  },    
  computed:{
      ...mapState([
          'username',
      ]),
      ...mapGetters([
          'isLogin',
      ])
  },
  created : async function(){
    // 수정일 경우,
    if(this.id!=null){
      try{
         // 작성되어있던 게시글 불러오기
          const { data } = await communityDetail(this.id)
          if(data.username != this.username){
            alert("수정 권한이 없는 사용자입니다.")
            // 게시글 리스트 페이지로 이동
            this.$router.push({ name: 'CommunityPage'});
          }

          this.data.title = data.title
          this.data.content = data.content

      }catch (error) {
        console.log(error.response)
      } 
     
    }
  },
  methods: {
    submit : async function(event){
      event.preventDefault()
      // 작성한 내용이 있을 때,
      if (this.data.title.trim()!="" 
      & this.data.content.trim()!=""){
        // 수정
        if(this.id){
          this.updatePost()
        }else{
          // 새 글 생성
          this.createPost()
        }
        
      }else{
        // 작성한 내용이 없을 때,
        alert ("제목 / 내용을 모두 작성해주세요.")
      }
    },
    createPost : async function(){
      try{
          // api/index.js 에 있는 axios 함수 호출. 
          // url은 파일에 지정되어 있음.
          await communityCreate(this.data)

          // 폼에 작성되어있던 내용 비우기          
          this.data = {
            title:'',
            content:''
          }

          // 게시글 리스트 페이지로 이동
          this.$router.push({ name: 'CommunityPage'});
          // 'PostDetailPage', params: { userId: pk }})

        }catch (error) {
          console.log(error.response)
        } 
    },
    updatePost : async function(){
      try{
          // api/index.js 에 있는 axios 함수 호출. 
          // url은 파일에 지정되어 있음.
          await communityUpdate(this.id, this.data)

          // 폼에 작성되어있던 내용 비우기          
          this.data = {
            title:'',
            content:''
          }

          // 수정한 게시글 페이지로 이동
          this.$router.push({ name: 'PostDetailPage', params: { id : this.id }})

        }catch (error) {
          console.log(error.response)
        } 
    }
  }
}
</script>

<style>

</style>