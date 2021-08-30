<template>
  <table class="table text-white mt-3">
  <thead>
    <tr class="table-dark">
      <th scope="col">No.</th>
      <th scope="col">Title</th>
      <th scope="col">Author</th>
      <th scope="col">created_at</th>
    </tr>
    <CommunityItem v-for="(post, idx) in posts" :key="idx" :post="post" />
  </thead>
  </table>
</template>

<script>
import { communityList } from '@/api/index'

import CommunityItem from './CommunityItem.vue'
export default {
    name:"CommunityList",
    components: { CommunityItem },
    created: async function(){
      try{
        // api/index.js 에 있는 axios 함수 호출. 
        // url은 파일에 지정되어 있음.
        const { data } = await communityList()

        // 갱신할 데이터
        this.posts = data

      }catch (error) {
        console.log(error.response)
      } 
    },
    data : function(){
        return {
            posts: null,
        }
    },
}
</script>

<style>

</style>