<template>
  <div class="MainContainer">
    <div class="background"></div>
    <div class="identifyWindow">
      <div class="title-auth">
        Авторизация
      </div>
      <div>
        <input v-model="userName" placeholder="UserName">
        <button v-on:click="submitUserName">Принять</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import config from '../../config/config';

export default {
  name: 'Authorization',
  data() {
    return {
      userName: '',
    };
  },
  methods: {
    handleSubmitSuccess(resp) {
      console.log(resp);
    },
    submitUserName() {
      console.log(this.message);
      axios.post(`${config.getApiUrl()}login`, {
        userName: this.userName,
      }).then(this.handleSubmitSuccess)
        .catch(this.handleSubmitSuccess);
    },
  },
};
</script>

<style scoped>
.title-auth {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 100%;
  text-align: center;
  display: flex;
  padding-top: 10px;
  font-size: 20px;
  justify-content: center;
  align-items: center;
}

.background {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0.75;
  background: gray;
  -webkit-filter: blur(10px);
  filter: blur(10px);
}

.identifyWindow {
  position: absolute;
  top: 20%;
  left: 30%;
  right: 30%;
  bottom: 30%;
  background: white;
  z-index: 1;
  border-radius: 10px;
}

.MainContainer {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
</style>
