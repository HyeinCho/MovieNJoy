<template>
  <ul class="ticket-review">
      <template v-if="ticketReview!=null">
      <div>
        <!-- Ticket SVG 시작 -->
        <svg class="ticket-shape" width="95%" xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 600 1200" preserveAspectRatio="xMidYMid meet">
        <defs>
        <linearGradient :id="'MyTicketColor'+movie.movie_pk" gradientTransform="rotate(65)">
          <stop offset="5%" class="gradient1" :stop-color="color1" />
          <stop offset="95%" class="gradient1" :stop-color="color2" />
        </linearGradient>
        </defs>
        <g xmlns="http://www.w3.org/2000/svg" width="100%" transform="translate(0,1200) scale(0.1,-0.1)" :fill="'url(#MyTicketColor'+movie.movie_pk+')'">
            <path d="M406 11988 c-3 -7 -7 -35 -10 -62 -19 -161 -172 -308 -335 -323 l-61 -6 0 -5597 0 -5597 61 -6 c167 -15 315 -162 337 -333 l7 -59 193 -3 c168 -2 192 -1 192 13 0 37 41 95 82 116 87 44 183 8 215 -82 l18 -49 181 0 182 0 6 31 c27 137 224 162 285 36 12 -24 21 -49 21 -55 0 -9 49 -12 184 -12 l184 0 7 37 c9 48 60 99 108 108 84 16 167 -31 187 -106 l11 -39 198 0 199 0 7 37 c9 48 60 99 108 108 84 16 167 -31 184 -103 l9 -37 179 -3 180 -2 18 50 c50 141 264 128 293 -19 l6 -31 183 0 183 0 5 30 c16 75 87 125 167 118 65 -7 106 -38 127 -99 l18 -49 196 0 197 0 6 31 c20 101 137 149 231 96 31 -18 44 -34 60 -75 l20 -52 181 0 181 0 6 59 c15 168 162 317 332 339 l60 7 0 5595 0 5595 -60 7 c-170 22 -317 171 -332 339 l-6 59 -181 0 -181 0 -20 -52 c-16 -41 -29 -57 -60 -75 -94 -53 -211 -5 -231 96 l-7 31 -196 0 -196 0 -18 -49 c-21 -61 -62 -92 -127 -99 -80 -7 -151 43 -167 118 l-5 30 -183 0 -182 0 -7 -31 c-20 -103 -137 -150 -232 -94 -35 20 -47 35 -61 75 l-18 50 -180 -2 -179 -3 -9 -37 c-17 -72 -100 -119 -184 -103 -48 9 -99 60 -108 108 l-7 37 -199 0 -198 0 -11 -39 c-20 -75 -103 -122 -187 -106 -48 9 -99 60 -108 108 l-7 37 -184 0 c-135 0 -184 -3 -184 -12 0 -6 -9 -31 -21 -55 -61 -126 -258 -101 -285 36 l-6 31 -182 0 -181 0 -18 -49 c-32 -90 -128 -126 -215 -82 -41 21 -82 79 -82 116 0 13 -26 15 -190 15 -144 0 -192 -3 -194 -12z"/>
        </g>
        <!-- 사각형 구분선 -->
        <rect x="8%" y="8%" width="84%" height="82%" :stroke="inkColor" stroke-width="4"/>
        <rect x="8%" y="8%" width="84%" height="56%" :stroke="inkColor" stroke-width="4"/>
        <rect x="8%" y="8%" width="84%" height="48%" :stroke="inkColor" stroke-width="4"/>
        <rect x="8%" y="8%" width="84%" height="24%" :stroke="inkColor" stroke-width="4"/>
        <!-- 상자 밖 상단 (로고 / 넘버) -->
        <text x="9%" y="7%" class="brand-font" :style="'fill:'+inkColor+';'" 
         dominant-baseline="top" text-anchor="start">CinemaNJoy</text>
        <text x="91%" y="7%" class="title" :style="'fill:'+inkColor+';'"  
        dominant-baseline="top" text-anchor="end" >No. {{ movie.id }} </text>
        <!-- 상단 영화 제목 텍스트 -->
        <text x="11%" y="12%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start" >Title</text>
        <text x="89%" y="12%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="end" >[{{ movie.release_date | year }}]</text>
        <template v-if="movie.title!=movie.subtitle">
            <text x="50%" y="20%" class="title eng-title" :style="'fill:'+inkColor+';'" 
            dominant-baseline="middle" text-anchor="middle" >{{ movie.subtitle }}</text>
            <text x="50%" y="24%" class="title" :style="'fill:'+inkColor+';'" 
            dominant-baseline="middle" text-anchor="middle" >{{ movie.title }}</text>
        </template>
        <template v-else>
            <text x="50%" y="22%" class="title eng-title" :style="'fill:'+inkColor+';'" 
            dominant-baseline="middle" text-anchor="middle" >{{ movie.title }}</text>
        </template>
        <!-- 중간 영화 정보 텍스트 -->
        <text x="11%" y="38%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">Director</text>
        <text x="35%" y="38%" class="text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">{{ movie.directors[0].name }}</text>
        <text x="11%" y="43%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">Cast</text>
        <text x="35%" y="43%" class="text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">{{ getCastLine1 }}</text>
        <text x="35%" y="47.5%" class="text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">{{ getCastLine2 }}</text>
        <text x="35%" y="52%" class="text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">{{ getCastLine3 }}</text>
        <!-- 내 평점 텍스트 -->
        <text x="11%" y="61.2%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">Rating</text>
        <text x="32%" y="60.5%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="middle" text-anchor="start"> {{ getStar }} </text>
        <!-- 내 리뷰 텍스트 -->
        <text x="11%" y="69%" class="title" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="start">Review</text>
        <text x="14%" y="75%" class="typed-text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="middle" text-anchor="left">{{ getReviewTitleLine1 }}</text>
        <text x="14%" y="82%" class="typed-text" :style="'fill:'+inkColor+';'" 
        dominant-baseline="middle" text-anchor="left">{{ getReviewTitleLine2 }}</text>
        
        <!-- 리뷰 날짜 -->
        <template v-if="ticketReview.created_at!=null">
        <text x="50%" y="94%" class="brand-font" :style="'fill:'+inkColor+';'" 
        dominant-baseline="top" text-anchor="middle"> {{ ticketReview.created_at | dotDateFormat }} </text>
        </template>
        </svg>
        <!-- Ticket SVG 끝 -->
      </div>
      </template>
      <!-- <li>{{ ticketReview.rating }}</li> -->
  </ul>
</template>

<script>
// import { loadMovieData } from '@/api/index'
import ColorThief from '@/../node_modules/colorthief/dist/color-thief.mjs'
export default {
    name:'TicketReviewItem',
    props:{
        ticketReview: Object,
        movie: Object,
        movie_id:Number,
    },
    data: function(){
        return{
            cast : "",
            cast_char_unit: 14,
            color1: "",
            color2: "",
            inkColor: "black",
            img_poster: null,
        }
    },
    watch:{
        movie:function(){
            for(let a of this.movie.actors){
                this.cast += a.name + ", "
            }
            let url_poster = 'https://image.tmdb.org/t/p/original'+this.movie.thumbnail
            this.img_poster = new Image()
            this.img_poster.addEventListener('load', this.pickColor )
            this.img_poster.crossOrigin = 'Anonymous'
            this.img_poster.src = url_poster
        },

    },
    created: function(){
        if(this.movie!=null){
            for(let a of this.movie.actors){
                this.cast += a.name + ", "
            }
            let url_poster = 'https://image.tmdb.org/t/p/original'+this.movie.thumbnail
            this.img_poster = new Image()
            this.img_poster.addEventListener('load', this.pickColor )
            this.img_poster.crossOrigin = 'Anonymous'
            this.img_poster.src = url_poster
        }
    },
    methods:{
        pickColor() {
            const rgbToHex = (r, g, b) => '#' + [r, g, b].map(x => {
                const hex = x.toString(16)
                return hex.length === 1 ? '0' + hex : hex
            }).join('')

            const colorThief = new ColorThief();
            // 단일 색상
            // let color = colorThief.getColor(this.img_poster)
            // this.color1 = rgbToHex(color[0],color[1],color[2])
            // this.color2 = rgbToHex(color[0],color[1],color[2])
            // 복수 색상
            let color = colorThief.getPalette(this.img_poster, 2)
            
            this.color1 = rgbToHex(color[0][0],color[0][1],color[0][2])
            this.color2 = rgbToHex(color[1][0],color[1][1],color[1][2])
            
            // 명도에 따른 글자 색상 지정
            const brightness = (0.21 * color[0][0]) + (0.72 * color[0][1]) + (0.07 * color[0][2])
            if (brightness<100){
                this.inkColor="black"
            }else{
                this.inkColor="white"
            }
        }
    },
    computed:{
        getStar:function(){
            let rating = this.ticketReview.rating * 1
            return "⭐".repeat(rating) + "☆".repeat(5-rating) + " [" + rating + " / 5]"
        },
        getReviewTitleLine1:function(){
            let l = this.ticketReview.content.length
            let s = this.ticketReview.content
            if(l < 12){
                return s
            }else{
                return s.substring(0,12)
            }
        },
        getReviewTitleLine2:function(){
            let l = this.ticketReview.content.length
            let s = this.ticketReview.content
            if(l < 12){
                return ""
            }else if(l < 24){
                return s.substring(12,l)
            }else{
                return s.substring(12,24)+"..."
            }
        },
        getCastLine1:function(){
            let l = this.cast.length
            let s = this.cast
            if(l < this.cast_char_unit){
                return s
            }else{
                return s.substring(0,this.cast_char_unit)
            }
        },
        getCastLine2:function(){
            let l = this.cast.length
            let s = this.cast
            if(l < this.cast_char_unit){
                return ""
            }else if(l < this.cast_char_unit*2){
                return s.substring(this.cast_char_unit,l)
            }else{
                return s.substring(this.cast_char_unit,this.cast_char_unit*2)
            }
        },
        getCastLine3:function(){
            let l = this.cast.length
            let s = this.cast
            if(l < this.cast_char_unit*2){
                return ""
            }else if(l < this.cast_char_unit*3){
                return s.substring(this.cast_char_unit*2,l)
            }else{
                return s.substring(this.cast_char_unit*2,this.cast_char_unit*3)+"..."
            }
        },
    },
    filters: {
        year: function (value) {
            return value.slice(0,4)
        },
        dotDateFormat: function(value){
            return value.replaceAll('-','. ')
        }
    }
}
</script>

<style scoped>
ul{
    padding: 0;
}
.ticket-review{
    list-style-type: none;
}
.ticket-shape{
    fill:url(#MyGradient)
}
.title {
    fill: white;
    font-size: 2em;
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 500;
}

/* web font CDN */
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Pattaya&display=swap');
@font-face {
    font-family: 'InkLipquid';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/InkLipquid.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@import url('https://fonts.googleapis.com/css2?family=Jost:ital,wght@1,700&family=Oswald:wght@300&display=swap');
.brand-font {
    font-family: 'Jost', sans-serif;
    fill: white;
    font-size: 2em;
}
.eng-title {
    font-family: 'Jost', sans-serif;
    fill: white;
    font-size: 2.5em;
}

.typed-text{
    fill: white;
    font-size: 4em;
    font-family: 'InkLipquid';
}
.text {
    fill: white;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 2.3em;
    font-weight: 300;
}

input[type="text"]
{
    background: transparent;
    border: none;
    font-family: 'InkLipquid';
    font-size: 3em;
    color: white;
}
</style>