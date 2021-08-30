import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    isSearchBarOnNav : true,
    username: '',
    token : null,
    user: null
  },
  mutations: {
    SET_USER_NAME(state, username){
      state.username = username
    },
    SET_TOKEN(state, token){
      state.token = token
      localStorage.setItem('jwt', token)
      this.dispatch('setUserName')
    },
    LOGOUT : function (state){
      localStorage.removeItem('jwt')
      state.token = null
      state.username = ''
    },
    LOGIN : function (state, token) {
      state.isLogin = true
      localStorage.setItem('jwt', token)
      state.token = token
      // this.dispatch('getUserInfo')
    },
    // SET_USER : function (state, user){
    //   state.user = user
    // }
  },
  actions: {
    logout : function({ commit }){
      commit('LOGOUT')
    },
    login : function({ commit }, token){
      commit('LOGIN', token)
    },
    setToken: function({commit}, token){
      commit('SET_TOKEN', token)
    },
    setUserName: function({commit, getters}){
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/username/',
        headers : getters.token_config
      })
      .then(res => {
        let user = res.data
        commit('SET_USER_NAME', user.username)
      })
      .catch(err => {
        console.log(err)
      })      
    },
    // getUserInfo : function({commit, getters}){
    //   axios({
    //     method: 'post',
    //     url: 'http://127.0.0.1:8000/accounts/userinfo/',
    //     headers : getters.token_config
    //   })
    //   .then(res => {
    //     let user = res.data
    //     // console.log(user)
    //     commit('SET_USER', user)
    //   })
    //   .catch(err => {
    //     console.log(err)
    //   })
    // }
  },
  modules: {
  },
  getters:{
    token_config : function (state) {
      const config = {
        Authorization: `JWT ${state.token}`
      }
      return config
    },
    isLogin(state){
      return state.username !== ''
    }
  },
  // 새로 고침해도 vuex 내용 저장
  plugins: [createPersistedState()],
})
