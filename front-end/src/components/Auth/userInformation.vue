<template>
  <div class="containerPersonInformation">
    <div>
      {{userName}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'userInformation',
  props: {
    userName: String,
  },
};
</script>

<style scoped>
.containerPersonInformation {
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 100px;
  background: red;
}
</style>
