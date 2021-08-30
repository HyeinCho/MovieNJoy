import Vue from 'vue'
import VueRouter from 'vue-router'
import BoxOfficePage from '@/views/BoxOfficePage'
import MoviesPage from '@/views/MoviesPage'
import CommunityPage from '@/views/CommunityPage'
import TicketboxPage from '@/views/TicketboxPage'
// import PhotoBoothPage from '@/views/PhotoBoothPage'
import DiscoveryPage from '@/views/DiscoveryPage'
import ProfilePage from '@/views/ProfilePage'
import SearchResultPage from '@/views/SearchResultPage'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'BoxOfficePage',
    component: BoxOfficePage
  },
  // 검색 페이지
  {
    path: '/search/:keyword',
    name: 'SearchResultPage',
    component: SearchResultPage
  },
  // 영화 페이지
  {
    path: '/movies',
    name: 'MoviesPage',
    component: MoviesPage
  },
  {
    path: '/movies/:id',
    name: 'MovieDetailPage',
    component: () => import ('@/views/MovieDetailPage'),
    props: true,
  },
  // 커뮤니티 페이지
  {
    path: '/community',
    name: 'CommunityPage',
    component: CommunityPage
  },
  {
    path: '/community/post/:id',
    name: 'PostDetailPage',
    component: () => import ('@/views/PostDetailPage'),
    props: true,
  },
  {
    path: '/community/new',
    name: 'PostCreatePage',
    component: () => import ('@/views/PostEditorPage'),
  },
  {
    path: '/community/post/:id/editor',
    name: 'PostUpdatePage',
    component: () => import ('@/views/PostEditorPage'),
    // props: true,
  },
  // 티켓박스 페이지
  {
    path: '/ticketbox',
    name: 'TicketboxPage',
    component: TicketboxPage
  },
  {
    path: '/ticketbox/ticket/:id',
    name: 'TicketDetailPage',
    component: () => import ('@/views/TicketDetailPage'),
  },
  {
    path: '/ticketbox/new/:id',
    name: 'TicketCreateFromMoviePage',
    component: () => import ('@/views/TicketEditorPage'),
  },
  // {
  //   path: '/ticketbox/new/',
  //   name: 'TicketCreatePage',
  //   component: () => import ('@/views/TicketEditorPage'),
  // },
  // {
  //   path: '/photobooth',
  //   name: 'PhotoBoothPage',
  //   component: PhotoBoothPage
  // },
  {
    path: '/discovery',
    name: 'DiscoveryPage',
    component: DiscoveryPage
  },
  // 유저 페이지
  {
    path: '/accounts/login',
    name: 'Login',
    component: () => import ('@/views/accounts/LoginPage'),
    // 코드 스플리팅 : 해당 페이지 url로 이동했을 때만 다이나믹 임포트.
  }, 
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: () => import ('@/views/accounts/SignupPage'),
  }, 
  {
    path: '/accounts/:username',
    name: 'ProfilePage',
    component: ProfilePage,
    props: true,
  }, 
  {
    path: '*',
    component: () => import ('@/views/NotFoundPage.vue'),
},
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
