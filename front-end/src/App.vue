<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
};
</script>

<style>
#app {
  width: 100%;
  height: 100%;
}

html {
  width: 100%;
  height: 100%;
}

body {
  width: 100%;
  height: 100%;
  margin: 0;
}
* {
 -moz-box-sizing: border-box; /* в Firefox нужен префикс */
    box-sizing: border-box;
}
</style>
