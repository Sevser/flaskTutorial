<template>
  <div class="main-container">
    <auth></auth>
  </div>
</template>

<script>
import Authorization from './Auth/Authorization';

export default {
  name: 'MainComponent',
  components: {
    'auth': Authorization,
  },
};
</script>

<style scoped>
  .main-container {
    position: relative;
    width:100%;
    height: 100%;
    background: yellow;
  }
</style>
