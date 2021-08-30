<template>
      <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <!-- 웹사이트 로고 -->
            <router-link to="/" class="navbar-brand">CinemaNJoy</router-link>
            <!-- 모바일 사이트 navbar 토글 아이콘 -->
            <button v-b-toggle.my-collapse class="navbar-toggler" type="button" data-bs-toggle="collapse" 
            data-bs-target="#navbarToggler" aria-controls="navbarToggler" 
            aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggler">
            <!-- NavBar 좌측 아이템들 -->
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                <router-link to="/" class="nav-link">BoxOffice</router-link>
                </li>
                <li class="nav-item">
                <router-link to="/movies" class="nav-link">Movies</router-link>
                </li>
                <li class="nav-item">
                <a class="nav-link" @click="goCommunity">Community</a>
                </li>
                <li class="nav-item">
                <router-link to="/ticketbox" class="nav-link">Ticketbox</router-link>
                </li>
                <li class="nav-item">
                <router-link to="/discovery" class="nav-link">Discovery</router-link>
                </li>
            </ul>
            <!-- NavBar 우측 아이템들 -->
            <ul class="navbar-nav ms-auto mb-lg-0">
                <!-- <template v-if="isSearchBarOnNav"> -->
                    <li class="nav-item">
                        <SearchBar class="align-center"/>
                    </li>
                <!-- </template> -->
                <li class="nav-item dropdown">
                    <!-- 로그인한 경우 보임 -->
                    <template v-if="isLogin">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    {{ username }}
                    </a>
                    <ul class="dropdown-menu dropdown-menu-dark dropdown-menu-end" aria-labelledby="navbarDropdown">
                        <li>
                            <router-link :to="{name:'ProfilePage', params :{username}}" class="dropdown-item"> <span>Profile</span> </router-link>
                        </li>
                        <li >
                            <button @click="logout" class="dropdown-item">Logout</button>
                        </li>
                    </ul>
                    </template>
                    <!-- 로그인하지 않은 경우 보임 -->
                    <template v-else>
                        <router-link to="/accounts/login" class="nav-link">Login</router-link>
                    </template>
                    
                </li>
            </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import SearchBar from './SearchBar.vue'

export default {
    name: 'NavBar',
    components: { SearchBar },
    date: function(){
        return{
            login_text:'Login',
        }
    },
    computed:{
        ...mapState([
            // 'isSearchBarOnNav',
            'username',
        ]),
        ...mapGetters([
            'isLogin',
        ])
    },
    methods: {
        logout: function () {
            this.$store.dispatch('logout')
            this.$router.push({ name: 'Login' })
        },
        goCommunity : function (){
            // 로그인 되어있을 경우, 커뮤니티 페이지로 이동
            if (this.isLogin){
                this.$router.push({ name: 'CommunityPage' })
            // 그렇지 않을 경우, 로그인 페이지로 이동
            }else{
                this.$router.push({ name: 'Login' })
            }
        }
    },
    created: function () {
        // (새로 고침 등으로) 로그인 토큰이 남아있을 경우, 자동 로그인
        const token = localStorage.getItem('jwt')
        if (token) {
            this.$store.dispatch('login', token)
        }
    }
    
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@1,700&family=Oswald:wght@300&display=swap');
/*  브랜드 로고 폰트 */
.navbar-brand {
    font-family: 'Jost', sans-serif;
}

a{
    cursor: pointer;
}

</style>