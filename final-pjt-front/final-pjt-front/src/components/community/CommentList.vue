<template>
  <div class="d-flex flex-column align-items-start">
    <hr>
    <CommentItem v-for="(comment, idx) in comments" :key="idx" :comment="comment" />
    <hr>
  </div>
</template>

<script>
import CommentItem from './CommentItem.vue'
export default {
  components: { CommentItem },
    name: "CommentList",
    props : {
      comments:Array,
    }
}
</script>

<style scoped>
hr{
  background-color:white;
  height: 1px;
}
</style>