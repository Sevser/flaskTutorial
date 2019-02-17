<template>
  <div class="pame-props-container">
    <div>
      <select v-model="selected">
        <option disabled value="">Выберите один из вариантов</option>
        <option v-for="(type, i) in typesGames" :key="i">{{type}}</option>
      </select>
      <select v-model="selectedSide">
        <option disabled value="">Выберите один из вариантов</option>
        <option v-for="(type, i) in typeSide" :key="i+10">{{type}}</option>
      </select>
    </div>
    <div>
      <div class="button-start-game" @click="startGame">Начать игру</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'setGameProperties',
  data() {
    return {
      typesGames: [
        'PlayAlone',
      ],
      typeSide: [
        'cross',
        'circle',
      ],
      selectedSide: '',
      selected: '',
    };
  },
  methods: {
    changeType(newType) {
      console.log(newType);
    },
    startGame() {
      if (!this.selected && !this.selectedSide) {
        // eslint-disable-next-line
        alert('выберете тип игры');
      } else {
        this.$bus.$emit('start-game', {
          typegame: this.selected,
          selectturn: this.selectedSide === 'cross' ? 1 : 2,
        });
      }
    },
  },
};
</script>

<style scoped>
.button-start-game {
  width: 100px;
  height: 40px;
  background-color: blue;
  color: yellow;
}

.pame-props-container {
  position: absolute;
  left: 800px;
  top: 0px;
}
</style>
