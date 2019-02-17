/* eslint-disable */
<template>
  <div class="containerUsers">
    <div>сущестующие пользователи</div>
    <div class="userItem" v-for="(user, id) in userList" :key="id">
      {{user.username}}
    </div>
    <div class="refreshButtonContainer" @click="updateListUser">
      <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 294.843 294.843" style="enable-background:new 0 0 294.843 294.843;" xml:space="preserve"><g><path d="M147.421,0c-3.313,0-6,2.687-6,6s2.687,6,6,6c74.671,0,135.421,60.75,135.421,135.421s-60.75,135.421-135.421,135.421S12,222.093,12,147.421c0-50.804,28.042-96.902,73.183-120.305c2.942-1.525,4.09-5.146,2.565-8.088c-1.525-2.942-5.147-4.09-8.088-2.565C30.524,41.937,0,92.118,0,147.421c0,81.289,66.133,147.421,147.421,147.421s147.421-66.133,147.421-147.421S228.71,0,147.421,0z"/><path d="M205.213,71.476c-16.726-12.747-36.71-19.484-57.792-19.484c-52.62,0-95.43,42.81-95.43,95.43s42.81,95.43,95.43,95.43c25.49,0,49.455-9.926,67.479-27.951c2.343-2.343,2.343-6.142,0-8.485c-2.343-2.343-6.143-2.343-8.485,0c-15.758,15.758-36.709,24.436-58.994,24.436c-46.003,0-83.43-37.426-83.43-83.43s37.426-83.43,83.43-83.43c36.894,0,69.843,24.715,80.126,60.104c0.924,3.182,4.253,5.011,7.436,4.087c3.182-0.925,5.012-4.254,4.087-7.436C233.422,101.308,221.398,83.809,205.213,71.476z"/><path d="M217.773,129.262c-2.344-2.343-6.143-2.343-8.485,0c-2.343,2.343-2.343,6.142,0,8.485l22.57,22.571c1.125,1.125,2.651,1.757,4.243,1.757s3.118-0.632,4.243-1.757l22.57-22.571c2.343-2.343,2.343-6.142,0-8.485c-2.344-2.343-6.143-2.343-8.485,0l-18.328,18.328L217.773,129.262z"/></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g><g></g></svg>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

import config from '../config/config';

export default {
  name: 'userList',
  data() {
    return {
      userList: [],
    };
  },
  methods: {
    handleSuccess(resp) {
      this.userList = resp.data.users;
    },
    handleError(resp) {
      console.log(resp);
    },
    updateListUser() {
      axios.post(`${config.getApiUrl()}getuser`, {
        action: 'getallusers',
      }).then(this.handleSuccess, this.handleError);
    },
  },
};
</script>

<style scoped>
.userItem {
  display: block;
  width: 100%;
  float: left;
  border: 2px solid;
  border-radius: 5px;
  margin-top: 32px;
  padding: 10px;
}

.containerUsers {
  position: absolute;
  top: 0;
  left: 0;
  width: 150px;
}

.refreshButtonContainer {
  position: absolute;
  right: 0;
  width: 32px;
  height: 32px;
}
</style>
