<template>
  <div class="gameContainer">
    <v-stage :config="configKonva">
      <v-layer>
        <!--<v-circle :config="configCircle"></v-circle>-->
        <v-rect @click="handleMouseClick" v-for="(config, i) in configRectField" :key="i+9" :config="config"></v-rect>
      </v-layer>
    </v-stage>
  </div>
</template>

<script>
export default {
  name: 'game',
  data() {
    return {
      configKonva: {
        width: 600,
        height: 600,
      },
      configRectField: [
        {
          x: 0,
          y: 0,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 0,
        },
        {
          x: 201,
          y: 0,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 1,
        },
        {
          x: 401,
          y: 0,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 2,
        },
        {
          x: 0,
          y: 201,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 3,
        },
        {
          x: 201,
          y: 201,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 4,
        },
        {
          x: 401,
          y: 201,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 5,
        },
        {
          x: 0,
          y: 401,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 6,
        },
        {
          x: 201,
          y: 401,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 7,
        },
        {
          x: 401,
          y: 401,
          width: 199,
          height: 199,
          fill: 'white',
          stroke: 'black',
          data: 8,
        },
      ],
      configsRectBorder: [
        {
          x: 199,
          y: 0,
          width: 2,
          height: 600,
          stroke: 'black',
        },
        {
          x: 399,
          y: 0,
          width: 2,
          height: 600,
          stroke: 'black',
        },
        {
          x: 0,
          y: 199,
          width: 600,
          height: 2,
          stroke: 'black',
        },
        {
          x: 0,
          y: 399,
          width: 600,
          height: 2,
          stroke: 'black',
        },
      ],
    };
  },
  methods: {
    handleMouseClick(event) {
      const index = event.target.attrs.data;
      this.configRectField[index].fill = 'red';
    },
  },
};
</script>

<style scoped>
.gameContainer {
  width: 600px;
  height: 600px;
  background: white;
}
</style>
