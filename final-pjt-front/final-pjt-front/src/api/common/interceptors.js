import store from '@/store/index';

export function setInterceptors(axiosService) {
    axiosService.interceptors.request.use(function (config) {
      // 요청을 보내기 전에 어떤 처리를 할 수 있다.
      const auth_config = {
        Authorization: `JWT ${store.state.token}`
      }
      config.headers = auth_config
      return config;
    }, function (error) {
      // 요청이 잘못되었을 때 에러가 컴포넌트 단으로 오기 전에 어떤 처리를 할 수 있다.
      return Promise.reject(error);
    });

    axiosService.interceptors.response.use(function (response) {
      // 서버에 요청을 보내고 나서 응답을 받기 전에 어떤 처리를 할 수 있다.
      return response;
    }, function (error) {
      // 응답이 에러인 경우에 미리 전처리할 수 있다.
      return Promise.reject(error);
    });

    return axiosService;
}