<template>
  <div class="d-flex flex-column align-items-center">
    <h1 class="brand-font mb-3">Sign Up</h1>
    <div class="w-25">
      <!-- <label for="username" class="form-label" >사용자 이름: </label> -->
      <input type="text" id="username" placeholder="user name" class="form-control mb-1" v-model="credentials.username">
      <!-- <label for="password" class="form-label">비밀번호: </label> -->
      <input type="password" id="password" placeholder="password" class="form-control mb-1" v-model="credentials.password">
      <!-- <label for="passwordConfirmation" class="form-label">비밀번호 확인: </label> -->
      <input type="password" id="passwordConfirmation" placeholder="password confirmation" class="form-control" 
      v-model="credentials.passwordConfirmation" @keyup.enter="signup(credentials)">
    </div>
    <button :disabled ="isNotValid" 
    class="btn brand-font mt-3" :class = "isNotValid? 'btn-outline-secondary':'btn-secondary'"
    @click="signup(credentials)">Sign Up</button>
  </div>
</template>

<script>
import { registerUser } from '@/api/index'
import { loginUser } from '@/api/index'
// import { validatePassword } from '@utils/validation';


export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    async signup () {
      try{
        await registerUser(this.credentials)
        // this.logMessage = `${data.user.username}님 회원 가입이 완료되었습니다.`;
        // this.$router.push({ name: 'Login' })

        //  가입 완료되면 바로 로그인 시켜주고 메인으로 리다이렉트
        this.login()

      } catch (error){
        console.log(error.response)
        // this.logMessage = error.response.data;
      } finally {
        this.initForm();
      }
    },
    async login(){
      try{
        const { data } = await loginUser(this.credentials)
        this.$store.dispatch('setToken', data.token)
        this.$router.push({ name: 'BoxOfficePage' })

      }catch (error) {
        console.log(error.response)
      } 
    },
    initForm() {
      this.username = ''
      this.password = ''
      this.passwordConfirmation = ''
    }
  },
  computed: {
      isNotValid() {
          return !this.credentials.password || !this.credentials.passwordConfirmation || !this.credentials.username
      }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@1,700&family=Oswald:wght@300&display=swap');
/*  브랜드 로고 폰트 */
.brand-font {
    font-family: 'Jost', sans-serif;
}

input{
  background: black;
  color: white;
}
</style>