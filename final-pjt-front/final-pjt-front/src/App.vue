<template>
  <div id="app">
    <NavBar class="nav"/>
    <transition name="fade" mode="out-in">
      <router-view :key="$route.fullPath" class="mt-3"/>
    </transition>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default({
  components: { 
    NavBar 
    },
  name: 'App'
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: black;
  min-height: 100%;
}
html, body{
  height: 100%;
}

.nav{
  z-index: 2;
}

/* 전체 font */
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@1,700&family=Noto+Sans+KR&display=swap');
* {
  font-family: 'Noto Sans KR', sans-serif;
}

/* fade 전환효과 */
.fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease-out; }
.fade-enter-from,.fade-leave-to { opacity: 0; }

/* slide-fade 전환효과 */
.slide-fade-enter { transform: translateX(10px); opacity: 0; } 
.slide-fade-enter-active, .slide-fade-leave-active { transition: all 0.2s ease; } 
.slide-fade-leave-to { transform: translateX(-10px); opacity: 0; }

</style>
