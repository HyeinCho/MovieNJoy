<template>
  <div class="boxoffice container">
    <h1 class="neonText">boxoffice</h1>
    <RecentMovieCuration/>
    <RecommendCuration class="my-5"/>
  </div>
</template>

<script>
import RecentMovieCuration from '../components/boxoffice/RecentMovieCuration.vue'
import RecommendCuration from '../components/boxoffice/RecommendCuration.vue'
export default {
  components: { RecentMovieCuration, RecommendCuration },
    name: 'BoxOfficePage',
    created : function(){
      console.log('%cCinemaNJoy', 'color: #cc90ff; font-size:3rem; background-color: #000; padding: 5px;');
      console.log('%c개발자 구직 중 (구인X)', 'color: #ffffff; font-size:1.5rem; background-color: #000; padding: 5px;');
      console.log('%c엔터빰', 'color: #cc90ff; font-size:1.5rem; background-color: #000; padding: 5px;');
    }
}
</script>

<style scoped>
.neonText {
    display: inline;
    color: #fff;
    text-shadow:
        0 0 7px #fff,
        0 0 10px #fff,
        0 0 21px #fff,
        0 0 42px #bc13fe,
        0 0 82px #bc13fe,
        0 0 92px #bc13fe,
        0 0 102px #bc13fe,
        0 0 151px #bc13fe;
}

h1 {
    animation: pulsate 1.5s infinite alternate;  
    border-bottom: 0.2rem solid #fff;
    padding: 0 0.2rem;
    /* border-radius: .4rem; */
    box-shadow: 0 0 .2rem #fff,
                0 0 .2rem #fff,
                0 0 2rem #bc13fe,
                inset 0 0 1.3rem #bc13fe; 
}

@keyframes pulsate {
    100% {

        text-shadow:
        0 0 4px #fff,
        0 0 11px #fff,
        0 0 19px #fff,
        0 0 40px #bc13fe,
        0 0 80px #bc13fe,
        0 0 90px #bc13fe,
        0 0 100px #bc13fe,
        0 0 150px #bc13fe;
    
    }
    
    0% {

        text-shadow:
        0 0 2px #fff,
        0 0 4px #fff,
        0 0 6px #fff,
        0 0 10px #bc13fe,
        0 0 45px #bc13fe,
        0 0 55px #bc13fe,
        0 0 70px #bc13fe,
        0 0 80px #bc13fe;

    }
}
</style>