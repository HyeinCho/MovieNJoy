<template>
    <div class='carousel'>
        <input checked='checked' class='carousel__activator' id='carousel-slide-activator-1' name='carousel' type='radio'>
        <input class='carousel__activator' id='carousel-slide-activator-2' name='carousel' type='radio'>
        <input class='carousel__activator' id='carousel-slide-activator-3' name='carousel' type='radio'>
        <div class='carousel__controls'>
            <label class='carousel__control carousel__control--forward' for='carousel-slide-activator-2'>
            👉
            </label>
        </div>
        <div class='carousel__controls'>
            <label class='carousel__control carousel__control--backward' for='carousel-slide-activator-1'>
            👈
            </label>
            <label class='carousel__control carousel__control--forward' for='carousel-slide-activator-3'>
            👉
            </label>
        </div>
        <div class='carousel__controls'>
            <label class='carousel__control carousel__control--backward' for='carousel-slide-activator-2'>
            👈
            </label>
        </div>
        <div class='carousel__screen'>
            <ul class="carousel__track">
                <MovieItem v-for="(movie, idx) in movies" :key="idx" :movie="movie"
                class="carousel__item carousel__item--mobile-in-1 carousel__item--tablet-in-3 carousel__item--desktop-in-6"/>
            </ul>
        </div>
    </div>
</template>

<script>
import MovieItem from './MovieItem.vue'
export default {
    name:'MovieCarouselList',
    components: { 
        MovieItem 
    },
    props:{
        movies: Array,
    },
}
</script>

<style>


.carousel {
  min-width: 900px;
  max-width: 1236px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 48px;
  padding-right: 48px;
  position: relative;
}

.carousel__activator {
  display: none;
}

.carousel__controls {
  display: none;
  align-items: center;
  justify-content: space-between;
  position: absolute;
  top: 0;
  right: 16px;
  left: 16px;
  bottom: 0;
}
.carousel__controls:first-of-type {
  justify-content: flex-end;
}
.carousel__controls:last-of-type {
  justify-content: flex-start;
}

.carousel__control {
  cursor: pointer;
  display: flex;
  align-items: center;
  background-color: #fff;
  color: #3d414a;
  border-radius: 100%;
  box-shadow: 0 2px 10px 0 rgba(33, 34, 36, 0.3);
  font-size: 24px;
  height: 48px;
  justify-content: center;
  transition: 0.3s all;
  width: 48px;
  z-index: 1;
}
.carousel__control:hover {
  -webkit-transform: scale(1.05);
          transform: scale(1.05);
}

.carousel__activator:nth-of-type(1):checked
~ .carousel__controls:nth-of-type(1) {
  display: flex;
}

.carousel__activator:nth-of-type(1):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(0%);
          transform: translateX(0%);
}

.carousel__activator:nth-of-type(2):checked
~ .carousel__controls:nth-of-type(2) {
  display: flex;
}

.carousel__activator:nth-of-type(2):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-100%);
          transform: translateX(-100%);
}

.carousel__activator:nth-of-type(3):checked
~ .carousel__controls:nth-of-type(3) {
  display: flex;
}

.carousel__activator:nth-of-type(3):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-200%);
          transform: translateX(-200%);
}

.carousel__activator:nth-of-type(4):checked
~ .carousel__controls:nth-of-type(4) {
  display: flex;
}

.carousel__activator:nth-of-type(4):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-300%);
          transform: translateX(-300%);
}

.carousel__activator:nth-of-type(5):checked
~ .carousel__controls:nth-of-type(5) {
  display: flex;
}

.carousel__activator:nth-of-type(5):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-400%);
          transform: translateX(-400%);
}

.carousel__activator:nth-of-type(6):checked
~ .carousel__controls:nth-of-type(6) {
  display: flex;
}

.carousel__activator:nth-of-type(6):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-500%);
          transform: translateX(-500%);
}

.carousel__activator:nth-of-type(7):checked
~ .carousel__controls:nth-of-type(7) {
  display: flex;
}

.carousel__activator:nth-of-type(7):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-600%);
          transform: translateX(-600%);
}

.carousel__activator:nth-of-type(8):checked
~ .carousel__controls:nth-of-type(8) {
  display: flex;
}

.carousel__activator:nth-of-type(8):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-700%);
          transform: translateX(-700%);
}

.carousel__activator:nth-of-type(9):checked
~ .carousel__controls:nth-of-type(9) {
  display: flex;
}

.carousel__activator:nth-of-type(9):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-800%);
          transform: translateX(-800%);
}

.carousel__activator:nth-of-type(10):checked
~ .carousel__controls:nth-of-type(10) {
  display: flex;
}

.carousel__activator:nth-of-type(10):checked
~ .carousel__screen
.carousel__track {
  -webkit-transform: translateX(-900%);
          transform: translateX(-900%);
}

.carousel__screen {
  overflow: hidden;
  margin-left: -16px;
  margin-right: -16px;
}

.carousel__track {
  font-size: 0;
  transition: all 0.3s ease 0s;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.carousel__item {
  display: inline-flex;
  padding-left: 16px;
  padding-right: 16px;
  vertical-align: top;
  white-space: normal;
}

.carousel__item--desktop-in-1 {
  width: 100%;
}

.carousel__item--desktop-in-2 {
  width: 50%;
}

.carousel__item--desktop-in-3 {
  width: 33.3333333333%;
}

.carousel__item--desktop-in-4 {
  width: 25%;
}

.carousel__item--desktop-in-5 {
  width: 20%;
}

</style>