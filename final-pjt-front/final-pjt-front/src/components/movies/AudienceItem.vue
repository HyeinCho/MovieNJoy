<template>
  <div>
      <p>{{ audience.title }}</p>
      <p><img :src="'http://via.placeholder.com/150/FFFFFF/000000/?text=' + audience.username" alt="audience-profile" class="profile-image"></p>
  </div>
</template>

<script>
export default {
    name:'AudienceItem',
    props:{
        audience: Object,
    }
}
</script>

<style scoped>
.profile-image {
    width: 50%;
    height: auto;
    border-radius: 50%;
    object-fit: cover;
    object-position: center right;
}
</style>