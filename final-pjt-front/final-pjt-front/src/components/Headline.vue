<template>
    <h3 class="title-style mb-3"> {{ title }} </h3>
</template>

<script>
export default {
    name:"Headline",
    props:{
        title:String,
    }
}
</script>

<style scoped>
.title-style{
    margin-top:3rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid white;
}
</style>