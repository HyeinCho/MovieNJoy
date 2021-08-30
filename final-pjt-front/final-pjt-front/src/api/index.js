import axios from 'axios'
// import store from '@/store/index';
import { setInterceptors } from './common/interceptors'

function createAxiosService() {
    const axiosService = axios.create({
      baseURL: process.env.VUE_APP_API_URL,
    });

    return axiosService
//    return setInterceptors(axiosService)
}

const axiosService = createAxiosService()

function createAuthAxiosService() {
    const axiosService = axios.create({
        baseURL: process.env.VUE_APP_API_URL,
    });
    return setInterceptors(axiosService)
}

const authAxiosService = createAuthAxiosService()


// accounts 앱 관련 함수

function registerUser(userData) {
    const url = "accounts/signup/"
    return axiosService.post(url, userData)
}

function loginUser(userData) {
    const url = "accounts/api-token-auth/"
    return axiosService.post(url, userData);
}

function getUsername() {
    const url = "accounts/username/"
    return axiosService.get(url);
}

function getUserInfo() {
    const url = "accounts/userinfo/"
    return axiosService.get(url);
}

function isSignup() {
    const url = "accounts/isSignup/"
    return axiosService.post(url);
}

function getProfile(username) {
    const url = "accounts/" + username + "/"
    return axiosService.post(url, username);
}

function userFollow(username, data) {
    const url = "accounts/" + username + "/follow/"
    return axiosService.post(url, data);
}

// movies app 관련 함수
// 영화 페이지 관련 함수

function loadMovieData(id){
    const url = "movies/"+id+"/"
    return axiosService.get(url);
}

function loadMovieViedo(id){ // 영화 트레일러 유튜브 링크
    const url = "movies/"+id+"/video/"
    return axiosService.get(url);
}

function loadMovieBestReviews(id){ // 해당 영화 베스트 리뷰
    const url = "movies/"+id+"/best_review/"
    return axiosService.get(url);
}

function loadMovieAllReviews(id){ // 특정 영화의 모든 리뷰 조회 (더보기 클릭 시)
    const url = "movies/reviews/"+id+"/"
    return axiosService.get(url);
}

function movieLike(id, data){ // 영화 좋아요 버튼
    const url = "movies/"+id+"/likes/"
    return axiosService.post(url, data);
}

function recommendAnother(id){ // 이 영화를 본 다른 사람들이 본 영화
    const url = "movies/"+id+"/another_movie/"
    return axiosService.get(url);
}


// 영화 검색 관련 함수
function loadMovies(){ // 검색하기 전 기본으로 로드되는 함수
    const url = "movies/popular/"
    return axiosService.get(url);
}


function searchMovies(keyword){ // 영화 검색
    const url = "movies/search/" + keyword + "/"
    return axiosService.get(url);
}


// 영화 메인 페이지 관련 함수
function nowMovies(){
    const url = "movies/now_playing/"
    return axiosService.get(url);
}

function recommendSimilar(id){
    const url = "movies/"+id+"/similar_movie/"
    return axiosService.get(url);
}

function recommendGenre(){
    const url = "movies/genre_recommend/"
    return axiosService.get(url);
}

// 리뷰 관련 함수

function reviewCreate(id, data){ // 생성
    const url = "movies/"+id+"/review/"
    return authAxiosService.post(url, data);
}

function reviewDetail(review_id){ // 조회
    const url = "movies/review/"+review_id+"/"
    return authAxiosService.get(url);
}

function reviewUpdate(movie_id, review_id){ // 수정
    const url = "movies/"+movie_id+"/review/"+review_id+"/"
    return axiosService.put(url);
}

function reviewDelete(review_id){ // 삭제
    const url = "movies/review/"+review_id+"/"
    return authAxiosService.delete(url);
}

function reviewLike(review_id, data){ // 리뷰 좋아요
    const url = "movies/review/"+review_id+"/likes/"
    return authAxiosService.post(url, data);
}

// ticketbox app 관련 함수
function userReviewsList(username){ // 특정 유저가 쓴 모든 리뷰 조회
    const url = "movies/"+username+"/user_reviews_list/"
    return authAxiosService.post(url, username);
}

function userMoviesList(username){ // 특정 유저가 좋아하는 모든 영화 조회
    const url = "movies/"+username+"/user_movies_list/"
    return authAxiosService.post(url, username);
}

// community app 관련 함수

// 결과는 리스트 (게시글 여러개)
// id: 게시글 id
// user: user_id
// title
// created_at
function communityList(){ // 전체 페이지
    const url = "community/"
    return authAxiosService.get(url);
}

// id: 게시글 id
// comment_set: 리스트 형태
// title
// created_at
// updated_at
// user: user_id
// like_users: 리스트 형태
function communityCreate(data){ // 생성
    const url = "community/create/"
    return authAxiosService.post(url, data);
}

// id: 게시글 id
// comment_set: 리스트 형태. 여기 안에 id, comment, user, article
// title
// created_at
// updated_at
// user: user_id
// like_users: 리스트 형태
function communityDetail(id){ // 조회
    const url = "community/"+id+"/"
    return authAxiosService.get(url);
}

// id: 게시글 id
// comment_set: 리스트 형태. 여기 안에 id, comment, user, article
// title
// created_at
// updated_at
// user: user_id
// like_users: 리스트 형태
function communityUpdate(id, data){ // 수정
    const url = "community/"+id+"/"
    return authAxiosService.put(url, data);
}

// [ "1번 리뷰가 삭제되었습니다" ]
function communityDelete(id){ // 삭제
    const url = "community/"+id+"/"
    return authAxiosService.delete(url);
}

// id: 게시글 id
// comment: 댓글
// user: user_id
// article: 해당 게시글
function commentCreate(article_id, data){ // 생성
    const url = "community/"+article_id+"/comment/"
    return authAxiosService.post(url, data);
}

// 결과는 리스트 (댓글들)
// id: 게시글 id
// comment: 댓글
// user: user_id
// article: 해당 게시글
function commentList(article_id){ // 조회
    const url = "community/"+article_id+"/comment/"
    return authAxiosService.get(url);
}

// id: 게시글 id
// comment: 댓글
// user: user_id
// article: 해당 게시글
function commentUpdate(article_id, comment_id, data){ // 수정
    const url = "community/"+article_id+"/comment/"+comment_id+"/"
    return authAxiosService.put(url, data);
}

// [ "1번 리뷰가 삭제되었습니다" ]
function commentDelete(article_id, comment_id){ // 삭제
    const url = "community/"+article_id+"/comment/"+comment_id+"/"
    return authAxiosService.delete(url);
}

// liked: 좋아요 유무
// likeCnt: 좋아요 갯수
function articleLike(article_id, data){ // 게시글 좋아요
    const url = "community/"+article_id+"/likes/"
    return authAxiosService.post(url, data);
}

// 디스커버리
function getDiscovery(){ // 랜덤한 영화의 리뷰들 얻어오기
    const url = "movies/discovery/"
    return authAxiosService.get(url);
}


// 함수 이름 등록
export { registerUser, loginUser, getUsername, getUserInfo, isSignup, getProfile, userFollow, 
    loadMovies, loadMovieData, loadMovieViedo, loadMovieBestReviews, loadMovieAllReviews, movieLike,
    searchMovies, nowMovies, 
    recommendAnother, recommendSimilar, recommendGenre, 
    reviewCreate, reviewDetail, reviewUpdate, reviewDelete, reviewLike, userReviewsList, userMoviesList,  
    communityList, communityCreate, communityDetail, communityUpdate, communityDelete, 
    commentCreate, commentList, commentUpdate, commentDelete, 
    articleLike, getDiscovery }