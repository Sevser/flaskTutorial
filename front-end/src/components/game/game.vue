<template>
  <div class="gameContainer">
    <v-stage :config="configKonva">
      <v-layer>
        <!--<v-circle :config="configCircle"></v-circle>-->
        <v-rect @click="handleMouseClick" v-for="(config, i) in configRectField"
                :key="i+9"
                :config="config"
                ref="rect"></v-rect>
        <v-circle v-for="(config, i) in configsCircle" :key="i+18" :config="config"></v-circle>
        <v-line v-for="(config, i) in configCross" :config="config" :key="i+27"></v-line>
      </v-layer>
    </v-stage>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';
import config from '../../config/config';

export default {
  name: 'game',
  data() {
    return {
      isCross: false,
      configKonva: {
        width: 600,
        height: 600,
      },
      configsCircle: [],
      configCross: [],
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
      fieldGame: [],
      idGame: null,
    };
  },
  computed: {
    ...mapGetters([
      'token',
    ]),
  },
  methods: {
    clearFields() {
      this.configsCircle = [];
      this.configCross = [];
    },
    createCircle(index) {
      return {
        index,
        y: 100 + (Math.floor(index / 3) * 199),
        x: 100 + ((index % 3) * 199),
        radius: 70,
        stroke: 'black',
        strokeWidth: 4,
        selectTurn: '',
      };
    },
    createCross(index) {
      return {
        points: [
          50 + ((index % 3) * 199),
          50 + (Math.floor(index / 3) * 199),
          100 + ((index % 3) * 199),
          100 + (Math.floor(index / 3) * 199),
          150 + ((index % 3) * 199),
          50 + (Math.floor(index / 3) * 199),
          100 + ((index % 3) * 199),
          100 + (Math.floor(index / 3) * 199),
          150 + ((index % 3) * 199),
          150 + (Math.floor(index / 3) * 199),
          100 + ((index % 3) * 199),
          100 + (Math.floor(index / 3) * 199),
          50 + ((index % 3) * 199),
          150 + (Math.floor(index / 3) * 199),
          100 + ((index % 3) * 199),
          100 + (Math.floor(index / 3) * 199),
        ],
        stroke: 'black',
        strokeWidth: 4,
        closed: 'true',
      };
    },
    makeTurn(index) {
      this.clearFields();
      const props = {
        space: index,
        action: 'maketurn',
      };
      axios.post(`${config.getApiUrl()}tiktactoe`, props)
        .then(this.handleMakeTurnSuccess, this.handleErrorMakeTurn);
    },
    handleErrorMakeTurn() {
      // eslint-disable-next-line
      console.log(error);
    },
    handleMakeTurnSuccess(resp) {
      console.log(resp.data);

      resp.data.spaces.forEach((space, index) => {
        if (space) {
          if (space === 1) {
            this.configCross.push(this.createCross(index));
          } else if (space === 2) {
            this.configsCircle.push(this.createCircle(index));
          }
        }
      });
    },
    handleMouseClick(event) {
      const index = event.target.attrs.data;
      this.makeTurn(index);
      // if (this.fieldGame.length === 9) {
      //   this.fieldGame = [];
      //   this.configCross = [];
      //   this.configsCircle = [];
      //   return;
      // }
      // if (this.fieldGame.find(field => field === index)) {
      //   return;
      // }
      // this.fieldGame.push(index);
      // if (this.isCross) {
      //   this.configCross.push(this.createCross(index));
      // } else {
      //   this.configsCircle.push(this.createCircle(index));
      // }
      // this.isCross = !this.isCross;
    },
    handleSuccessCreateGame(resp) {
      if (resp.data.status === 'success') {
        this.idGame = resp.data.idGame;
        this.$bus.$emit('game:created', { idGame: this.idGame });
        this.clearFields();
      } else {
        // eslint-disable-next-line
        alert('что то пошло не так не удалось создать игру');
      }
    },
    handleErrorCreateGame(error) {
      // eslint-disable-next-line
      console.log(error);
    },
    startGame(props) {
      // eslint-disable-next-line
      props.action = 'play';
      // eslint-disable-next-line
      props.token = this.token;
      this.selectTurn = props.selectturn;
      axios.post(`${config.getApiUrl()}tiktactoe`, props)
        .then(this.handleSuccessCreateGame, this.handleErrorCreateGame);
    },
  },
  mounted() {
    this.$bus.$on('start-game', this.startGame);
  },
};
</script>

<style scoped>
.gameContainer {
  position: absolute;
  left: 200px;
  width: 600px;
  height: 600px;
  background: white;
}
</style>
