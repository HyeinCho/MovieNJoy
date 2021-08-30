<template>
  <div class="d-flex flex-column align-items-center">
    <h1 class="brand-font mb-3">Login</h1>
    <div class="w-25">
      <!-- <label for="username">사용자 이름: </label> -->
      <input type="text" id="username" placeholder="user name" class="form-control mb-1" v-model="credentials.username">
      <!-- <label for="password">비밀번호: </label> -->
      <input type="password" id="password" placeholder="password" class="form-control" v-model="credentials.password" @keyup.enter="login">
    </div>
    <button @click="login" class="btn btn-secondary mt-3">로그인</button>
    <hr>
    <p>아직 CinemaNJoy의 회원이 아니신가요?</p>
    <router-link to="/accounts/signup" class="nav-link brand-font">Sign Up</router-link>
  </div>
</template>

<script>
// import axios from 'axios'
import { loginUser } from '@/api/index'
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    async login(){
      try{
        const { data } = await loginUser(this.credentials)
        this.$store.dispatch('setToken', data.token)
        this.$router.push({ name: 'BoxOfficePage' })

      }catch (error) {
        console.log(error.response)
      } 
      // finally {

      // }
      
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@1,700&family=Oswald:wght@300&display=swap');
/*  브랜드 로고 폰트 */
.brand-font {
    font-family: 'Jost', sans-serif;
}
</style>