<template>
  <div class="container w-50">
    <!-- 버튼 내비게이션 -->
      <div class="d-flex flex-row justify-content-between mb-3">
        <router-link :to="{ name: 'CommunityPage'}">
          <button class="btn btn-sm btn-outline-secondary">
            <i class="fas fa-arrow-left"></i> 돌아가기
          </button>
        </router-link>
        <!-- 작성자와 유저가 일치할 때 보이는 버튼 -->
        <div v-if="username==this.article.username"
         class="btn-group" role="group">
          <!-- 글 수정 버튼 -->
          <button class="btn btn-sm btn-outline-secondary"
          @click="updateArticle">Edit</button>
          <!-- 글 삭제 버튼 -->
          <button class="btn btn-sm btn-outline-secondary" 
          @click="deleteArticle">Delete</button>
        </div>
      </div>
      <!-- 본문 -->
      <PostDetail :post="article" />
      <CommentList :comments="article.comment_set"/>
      <CommentEditor :pk="article.id" />
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import { communityDetail, communityDelete, commentList } from '@/api/index'
import CommentEditor from '../components/community/CommentEditor.vue'
import CommentList from '../components/community/CommentList.vue'
import PostDetail from '../components/community/PostDetail.vue'
export default {
    name:"PostDetailPage",
    components: { PostDetail, CommentList, CommentEditor },
    created: async function() {
      //   넘겨준 article Pk 기준으로
      this.article_id = this.$route.params.id;
      this.loadPost()
    },
    computed:{
      ...mapState([
          'username',
      ]),
      ...mapGetters([
          'isLogin',
      ])
  },
    data: function () {
      return {
        article_id : 1,
        article: null,
        comments: null,
      }
    },
    methods:{
      // 게시글 불러오기
      async loadPost(){
        try {
          // axios 요청으로 데이터를 받아온다.
          const { data } = await communityDetail(this.article_id)
          this.article = data
        }
        catch(error) {
          console.log(error.response)
        }
      },
      // 게시글 삭제
      updateArticle(){
        // 게시글 수정 페이지로 이동
        this.$router.push({ name: 'PostUpdatePage'});
      },
      // 게시글 삭제
      async deleteArticle(){
        await communityDelete(this.article_id)
        // 게시글 리스트 페이지로 이동
        this.$router.push({ name: 'CommunityPage'});
      },
      // 댓글 다시 불러오기
      reloadComments(){
        this.loadComments()
      },
      // 댓글 불러오기
      loadComments: async function() {
        try {
          // axios 요청으로 데이터를 받아온다.
          const { data } = await commentList(this.article_id)
          this.comments = data
        }
        catch(error) {
          console.log(error.response)
        }
      },
    }
}
</script>

<style>

</style>