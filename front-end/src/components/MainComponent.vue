<template>
  <div class="main-container">
    <auth v-if="!isAuth"></auth>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import Authorization from './Auth/Authorization';

export default {
  name: 'MainComponent',
  data() {
    return {
      isAuth: false,
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
  components: {
    'auth': Authorization,
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
