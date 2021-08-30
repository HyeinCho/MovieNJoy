<template>
  <div class="row d-flex justify-content-center">
    <AudienceItem class="col-3" v-for="(audience, idx) in audiences" :key="idx" :audience="audience"/>
  </div>
</template>

<script>
import AudienceItem from './AudienceItem.vue'
export default {
    name:'AudienceList',
    components: { AudienceItem },
    props : {
        audiences:Array,
    }
}
</script>

<style>

</style>