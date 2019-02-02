<template>
  <div class="MainContainer">
    <div class="background"></div>
    <div class="identifyWindow">
      <div class="title-auth">
        Авторизация
      </div>
      <div>
        <div class="newUserContainer">
          <div class="userFieldTitle">Создать пользователя</div>
          <div class="newUserFieldContainer">
            <div class="userFieldTitle">UserName</div>
            <input type="text" v-model="userNameRegistration" placeholder="UserName">
          </div>
          <div class="newUserFieldContainer">
            <div class="userFieldTitle">Password</div>
            <input type="password" v-model="passwordRegistration" placeholder="Password">
          </div>
          <button class="registrationButton" v-on:click="registerNewUser">Принять</button>
        </div>
        <div class="newUserContainer">
          <div class="userFieldTitle">Залогиниться</div>
          <div class="newUserFieldContainer">
            <div class="userFieldTitle">UserName</div>
            <input type="text" v-model="userNameLogIN" placeholder="UserName">
          </div>
          <div class="newUserFieldContainer">
            <div class="userFieldTitle">Password</div>
            <input type="password" v-model="passwordLogIN" placeholder="Password">
          </div>
          <button class="registrationButton" v-on:click="submitUserName">Принять</button>
        </div>
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
      userNameRegistration: '',
      passwordRegistration: '',
      userNameLogIN: '',
      passwordLogIN: '',
    };
  },
  methods: {
    handleSuccess(resp) {
      this.$store.dispatch('setToken', resp.data.token);
      this.$emit('setUserName', resp.data.username);
    },
    handleError(resp) {
      throw new Error(resp.data);
    },
    registerNewUser() {
      axios.post(`${config.getApiUrl()}login`, {
        action: 'registration',
        username: this.userNameRegistration,
        password: this.passwordRegistration,
      }).then(this.handleSuccess, this.handleError);
    },
    submitUserName() {
      axios.post(`${config.getApiUrl()}login`, {
        action: 'login',
        username: this.userNameLogIN,
        password: this.passwordLogIN,
      }).then(this.handleSuccess, this.handleError);
    },
  },
};
</script>

<style scoped>
.registrationButton {
  width: calc(100% - 40px);
}

.userFieldTitle {
  text-align: center;
}

.newUserFieldContainer {
  width: calc(100% - 40px);
  position: relative;
}

.newUserFieldContainer > input {
  width: 100%;
}

.newUserContainer {
  float: left;
  position: relative;
  width: 50%;
}

.newUserContainer > * {
  margin: 10px 20px;
}

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
