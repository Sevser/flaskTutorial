<template>
  <div class="containerPersonInformation">
    <div>
      {{userName}}
    </div>
    <div>
      {{idGame}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'userInformation',
  props: {
    userName: String,
    idGame: null,
  },
  methods: {
    setGameInfo(data) {
      this.idGame = data.idGame;
    },
  },
  mounted() {
    this.$bus.$on('game:created', this.setGameInfo);
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
