<template>
  <div>
      <div class="d-flex align-items-center justify-content-center mb-3">
        <h2 class="mb-0">{{ user.username }}</h2>
        <!-- 본인이 아닐 때만 follow 버튼 표시 -->
        <template v-if="user.username!=username">
        <button v-if="follow" class="btn btn-outline-light ms-3"
         @click="ToggleFollow"> Unfollow </button>
        <button v-else class="btn btn-light btn-outline-dark ms-3"
         @click="ToggleFollow"> Follow </button>
        </template>
      </div>
      <h5 class="mb-3"> {{ user.introduce }} </h5>
      <p class="my-0">팔로워 <span v-text="followers"></span></p>
      <p class="my-0">팔로잉 <span v-text="followings"></span></p> 
  </div>
</template>

<script>
import { userFollow } from '@/api/index'
import { mapState, mapGetters } from 'vuex'
export default {
    name:"UserInfo",
    props:{
        user:Object,
    },
    data: function () {
      return {
        follow: false,
        followers: 0,
        followings: 0,
      }
    },
    computed:{
        ...mapState([
            'username', // 팔로우 여부 확인을 위한 유저이름
        ]),
        ...mapGetters([
            'isLogin',
        ])
    },
    created: function () {
      this.profile_name = this.$route.params.username
      this.loadFollow(false)
    },
    methods:{
      loadFollow: async function (flag) {
        if (!this.isLogin ) {
          this.$router.push({ name: 'Login' })
        }else{
          try {
          const { data } = await userFollow(this.profile_name, {'login_user': this.username, 'flag': flag})

          this.follow = data.followed
          this.followers = data.follower
          this.followings = data.following

          } catch (error) {
            console.log(error.response)
          }
        }
      },
      ToggleFollow: function () {
        this.loadFollow(true)
      }
    },
}
</script>

<style>

</style>