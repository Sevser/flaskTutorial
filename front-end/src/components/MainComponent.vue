<template>
  <div class="main-container">
    <div v-if="isAuth">
      <userInfo :userName="userName"></userInfo>
      <game></game>
      <userList></userList>
      <gameProp></gameProp>
    </div>
    <auth v-if="!isAuth" @setUserName="setUserName"></auth>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import Authorization from './Auth/Authorization';
import userInfo from './Auth/userInformation';
import game from './game/game';
import userList from './userList';
import gameProp from './game/setGameProperties';

export default {
  name: 'MainComponent',
  components: {
    'auth': Authorization,
    userInfo,
    game,
    userList,
    gameProp,
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
}
</style>
