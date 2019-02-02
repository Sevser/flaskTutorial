import 'es6-promise/auto';
import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import App from './App';
import router from './router';
import store from './store';

Object.defineProperty(Vue.prototype, '$bus', {
  get() {
    return this.$root.bus;
  },
});

Vue.use(Vuex);
Vue.use(VueRouter);
Vue.config.productionTip = false;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  data: {
    bus: new Vue({}),
  },
  components: { App },
  template: '<App/>',
  store,
});
