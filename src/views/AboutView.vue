<template>
  <div>
    <div class="container-data">
      <div class="farmerDashboard">
        <div class="input-data">
          <div class="formtitle">
            <span>Enter Data</span>
          </div>
          <div class="responseContainer">
            <div class="response" v-for="(response, index) in errArray" :key="index">
              {{ response }}
            </div>
          </div>
          <input type="text" v-model="temp" placeholder="temperature" />
          <input type="text" v-model="hum" placeholder="humidity" />
          <input type="text" v-model="ph" placeholder="ph" />
          <input type="text" v-model="rainfall" placeholder="rainfall" />
          <button class="data-details-btn" @click="sendData">SEND DETAILS</button>
        </div>
        <div class="output-data">
          <div class="Sweetable-cropPrediction">
            <div class="crop-title">
              best crop
              <span class="value">{{ predicted }}</span>
            </div>
            <div class="result-reason" v-html="plantInfo"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      temp: "",
      hum: "",
      ph: "",
      rainfall: "",
      errArray: [],
      predicted: "",
      plantInfo: "",
    };
  },
  methods: {
    sendData() {
      this.errArray = [];
      let data = {
        temp: this.temp,
        humidity: this.hum,
        ph: this.ph,
        rainfall: this.rainfall,
      };
      let checkdata = [this.temp, this.hum, this.ph, this.rainfall];
      let response = [
        "-Temperature required *",
        "-Humidity required *",
        "-Ph required *",
        "-Rainfall needed *",
      ];
      if (
        this.temp == "" ||
        this.humidity == "" ||
        this.ph == "" ||
        this.rainfall == ""
      ) {
        for (let i = 0; i < checkdata.length; i++) {
          if (checkdata[i] == "") {
            this.errArray.push(response[i]);
          }
        }
      } else {
        // submit data
        this.errArray.push();
        axios.post("/team-project/4.1", data).then((res) => {
          this.predicted = res.data.data["predicted"];
          this.plantInfo = res.data.data["predictedMoreInfo"];
        });
      }
    },
  },
};
</script>

<style scoped>
* + * {
  padding: 0;
  margin: 0;
}

.farmerDashboard {
  /* padding: 10rem; */

  display: grid;
  grid-template-columns: repeat(2, 1fr);
  padding: 2rem;
}

.input-data {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 2rem;
}

.input-data input {
  width: 90%;
  margin: auto;
  height: 3.5rem;
  border-radius: 0.5rem;
  border: 1px solid green;
  background: none;
  padding: 0.2rem;
  text-align: center;
  color: green;
}

.input-data input::placeholder {
  color: white;
  font-size: large;
  text-transform: uppercase;
}
.output-data,
.input-data {
  border: 1px solid green;
  box-shadow: 0px 0px 15px green;
}
.output-data {
  margin-left: 0.5rem;
  padding: 4rem;
}

.crop-title {
  text-transform: uppercase;
  font-weight: bold;
  font-size: large;
}
.crop-title .value {
  color: maroon;
  text-transform: uppercase;
  font-weight: bold;
  font-size: large;
}
.data-details-btn {
  padding: 1rem;
  background: black;
  color: green;
  border: 1px solid white;
  border: 1px solid orange;
  font-weight: bold;
}
.data-details-btn:active {
  transform: scale(0.9);
}
.response {
  color: red;
}

@media (max-width: 400px) {
  .farmerDashboard {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>
