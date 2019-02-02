import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App';
import router from './router';

Object.defineProperty(Vue.prototype, '$bus', {
  get() {
    return this.$root.bus;
  },
});

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
});
