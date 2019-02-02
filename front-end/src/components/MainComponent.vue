<template>
  <div class="main-container">
    <auth v-if="!isAuth" @setUserName="setUserName"></auth>
    <userInfo v-if="isAuth" :userName="userName"></userInfo>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import Authorization from './Auth/Authorization';
import userInfo from './Auth/userInformation';

export default {
  name: 'MainComponent',
  components: {
    'auth': Authorization,
    userInfo,
  },
  data() {
    return {
      isAuth: false,
      userName: '',
    };
  },
  computed: {
    ...mapGetters([
      'token',
    ]),
  },
  watch: {
    // eslint-disable-next-line
    token: function (newVal) {
      if (newVal) {
        this.isAuth = true;
      } else {
        this.isAuth = false;
      }
    },
  },
  methods: {
    setUserName(userName) {
      this.userName = userName;
    },
  },
};
</script>


<style scoped>
.main-container {
  position: relative;
  width: 100%;
  height: 100%;
  background: yellow;
}
</style>
