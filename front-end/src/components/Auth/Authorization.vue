<template>
  <div class="MainContainer">
    <div class="background"></div>
    <div class="identifyWindow">
      здесь будет блок авторизации
    </div>
  </div>
</template>

<script>
export default {
  name: 'Authorization',
};
</script>

<style scoped>
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
  background: blue;
  z-index: 1;
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
