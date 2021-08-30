<template>
    <form class="d-flex">
        <div class="search">
            <i class="fas fa-search"></i>
            <input @keydown.enter.prevent="search" v-model="keyword"
             class="form-control me-2" type="search" placeholder="Search" 
             aria-label="Search">
        </div>
        <!-- <button class="btn btn-outline-light" type="submit"><i class="fas fa-search"></i></button> -->
    </form>
</template>

<script>
export default {
    name:'SearchBar',
    data: function(){
        return{
            keyword:'',    // 검색어
        }
    },
    methods: {
        search : function(event){
            event.preventDefault()
            this.$router.push({ name: 'SearchResultPage', params: { keyword : this.keyword } })
            this.$router.go(this.$router.currentRoute)
        }
    }
}
</script>

<style scoped>
/* 모바일 모드 */
.search {
    width: 100%;
}
.search input {
    text-indent: 25px;
    float: right;
}
.search .fa-search {
    color: grey;
    position: absolute;
    top: 16.7rem;
    left: 1rem;
}


/* 데스크탑 모드 */
@media (min-width: 992px){
    .search {
        position: relative;
        box-shadow: 0 0 40px rgba(51, 51, 51, .1)
    }
    .search input {
        text-indent: 25px;
        width: 80%;
        float: right;
        transition: all ease-in-out 0.5s 0s;
    }
    .search input:focus{
        width: 100%;
    }
    .search:focus-within .fa-search{
    top: 30%;
    left: 2%;
    }
    .search .fa-search {
    color: grey;
    position: absolute;
    top: 30%;
    left: 22%;
    transition: all ease-in-out 0.5s 0s;
    }
}



</style>