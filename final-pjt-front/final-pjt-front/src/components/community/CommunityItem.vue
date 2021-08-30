<template>
    <tr>
      <!-- 글 번호 -->
      <th scope="row" v-text="post.id">1</th>
      <!-- 글 제목 -->
      <td>
      <router-link :to="{ name: 'PostDetailPage', params: { id: post.id } }" class="text-white text-decoration-none" >
          <span v-text="post.title"> </span>
      </router-link>
      <!-- 글 작성자 -->
      </td>
      <td>
        <router-link :to="{ name: 'ProfilePage', params: { username: post.author } }" class="text-white text-decoration-none">
          <span v-text="post.author"></span>
        </router-link>
      </td>
      <!-- 글 작성시간 -->
      <td>{{ post.created_at | timeDisplay }}</td>
    </tr>
</template>

<script>
export default {
    name: "CommunityItem",
    props:{
        post: Object,
    },
    created:function(){
        
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

<style>

</style>