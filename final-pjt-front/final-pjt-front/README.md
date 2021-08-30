# final-pjt-front

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).







### B. 다영 진행 사항 및 어려운 점

##### **개발환경 설정**

* 프로젝트 생성 `vue create final-pjt-front`

* `.gitignore` 파일 설정

* 필요 라이브러리 임포트

  ```bash
  vue add router
  vue add vuex
  npm i axios
  npm i -g npm
  npm i --save lodash
  npm i bootstrap-vue
  ```

* **src/main.js** 에 bootstrap 추가

  ```js
  import BootstrapVue from 'bootstrap-vue'
  import 'bootstrap/dist/css/bootstrap.min.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  
  Vue.use(BootstrapVue)
  ```



##### NavBar

* **components/NavBar.vue** 추가

  * `router-link`는 NavBar.vue에, `router-view`는 App.vue에 있음.

* **bootstrap5 NavBar** 추가 및 dark 테마로 수정

  * **App.vue** 에서 배경 색상 black으로 지정
    (화면 최하단까지 배경색상이 렌더되지 않는 문제는 다음과 같이 수정)

    ```css
    #app {
      /* 생략 */
      color: white;
      background: black;
      height: 100%;
    }
    html, body{
      height: 100%;
    }
    ```

* navbar-brand 폰트 Jost 700 으로 지정

  * Google Font CDN

**[미해결 이슈]**

* `browser-width`가 일정이하일 때 햄버거 버튼을 눌러도 확장되지 않는 문제 발생



##### SearchBar

* **Vuex**의 state인 `isSearchBarOnNav`가 `false`이면 NavBar의 searchbar 표시 X

* focus 되면 서서히 창이 커지는 CSS 애니메이션 적용

  ```css
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
  .search .fa-search {
      color: grey;
      position: absolute;
      top: 30%;
      left: 22%;
      transition: all ease-in-out 0.5s 0s;
  }
  .search:focus-within .fa-search{
      top: 30%;
      left: 2%;
  }
  ```

  

##### Page (vue-router)

* **views/**에 `BoxOfficePage.vue`, `MoviesPage.vue`, `CommunityPage.vue`, `TicketboxPage.vue`, `PhotoBoothPage.vue`, `DiscoveryPage.vue`, `ProfilePage.vue`

  * components와 혼동을 피하기 위해 router 하위에 생기는 view들은 이름 끝에 **Page**를 붙이기로 한다.

* **router/index.js** 에 routes 추가

* **router-view** 이동에 대해 `fade transition ` 효과 추가

  ```vue
  <!-- 생략 -->
  <transition name="fade" mode="out-in">
        <router-view/>
  </transition>
  
  <style>
  /* fade 전환효과 */
  .fade-enter-active, .fade-leave-active { transition: opacity 0.5s ease-out; }
  .fade-enter-from,.fade-leave-to { opacity: 0; }
  </style>
  ```

**[미해결 이슈]**

* id나 pk를 갖는 페이지 이동 방법

  https://router.vuejs.org/kr/guide/essentials/dynamic-matching.html

  https://router.vuejs.org/kr/guide/essentials/passing-props.html



##### BoxOffice 페이지 - `BoxOfficePage.vue`, `RecentMovieCuration.vue`, `MovieList.vue`, `MovieItem.vue`

* Title Logo
* `RecentMovieCuration.vue` 생성
  * `MovieList.vue` : Movie Item에 `v-for`로  movies를 돌며 movie 오브젝트를 전달
  * `MovieItem.vue` 생성 : props로 전달받은 Movie를 렌더



##### Movies Page - `MoviesPage.vue`, `MovieInfo.vue`

* 영화 정보의 좌우 커튼 형태 구현

  ```vue
  <div class="d-flex align-items-stretch">
      <div class="curtain"></div>
      <MovieInfo :movie="movie" class="movie-info"/>
      <div class="curtain"></div>
  </div>
  
  <style scoped>
  .curtain{
    display: float;
    width: 10%;
    height: auto;
    background-image: url('../assets/red_curtain.jpg');
    background-repeat: repeat;
    background-size: auto 120%;
  }
  </style>
  ```

* 커튼 이미지 위에 black-transparnet linear gradient 추가

* 영화 정보 표시 구현

* 하트 토글 구현

**[미해결 이슈]**

* dark-blur background 우선순위 문제 (영화정보 위를 덮어버림)
* 창 크기 줄이면 하단에 검은 background 안 생기는 부분 존재
  * `#app`의 css를 `min-height: 100%;` 로 수정
* 영화포스터 Zoom 기능 
  * https://www.codesdope.com/blog/article/mouse-rollover-zoom-effect-on-images/
  * https://css-tricks.com/animate-a-container-on-mouse-over-using-perspective-and-transform/



##### MoviePage (TicketReviews) - `TicketReviewList.vue`, `TicketReviewItem.vue`

* `TicketReviewList.vue`, `TicketReviewItem.vue` 생성

* TicketReview Gradient 배경 적용
  https://cssgradient.io/
* 

**[미해결 이슈]**

* 포스터 색상에 따른 티켓 색상
  http://jsfiddle.net/xLF38/818/
  https://github.com/lokesh/color-thief



#### TicketReviewEditor

* 움직이는 별점 구현

  

##### MoviePage (Audiences) - `AudienceList.vue`, `AudienceItem.vue`

* `AudienceList.vue`, `AudienceItem.vue` 생성



##### CommunityPage - `TicketPosterItem.vue`, `TicketReviewList.vue`

*  `TicketPosterItem.vue`, `TicketReviewList.vue` 생성



##### CommunityPage (Review Detail)

* 모달?
* 미진행



##### TicketboxPage - `TicketBothList.vue`, `TicketBothItem.vue`

* `TicketBothList.vue`, `TicketBothItem.vue` 생성



##### Photobooth Page

* 미진행



##### ProfilePage - `AudienceItem.vue`, `UserInfo.vue`, `FavoriteMovie.vue`, `Headline.vue`, `TicketPosterList.vue`, `TicketReviewList`

* `AudienceItem.vue`, `UserInfo.vue`, `FavoriteMovie.vue`, `Headline.vue`, `TicketPosterList.vue`, `TicketReviewList` 생성



#### Login

* 새로 고침할 때마다 로그인이 풀리는 문제
  * 새로고침할 때마다 vuex의 값이 초기화된다. -> `vuex-persistedstate`
  * https://uxgjs.tistory.com/207



#### SignUp

