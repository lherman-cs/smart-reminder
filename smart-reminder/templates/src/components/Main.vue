<template>
  <div>
    <div class="row d-flex justify-content-center">
      <div class="btn-group btn-group-toggle" data-toggle="buttons">
        <label class="btn btn-lg btn-secondary" :class="{ active: isActive }" @click="onClickOn()">
          <input type="radio"> On
        </label>
        <label class="btn btn-lg btn-secondary" :class="{ active: !isActive }" @click="onClickOff()">
          <input type="radio"> Off
        </label>
      </div>
    </div>
    <div class="row mt-5 mb-5">
      <img :src="imgSrc">
    </div>
  </div>
</template>

<script>
export default {
  name: "Main",
  data() {
    return {
      isActive: true,
      imgSrc:
        "https://cdn3.iconfinder.com/data/icons/communication-2-3/63/alarm-256.png"
    };
  },
  methods: {
    onClickOn: function() {
      if (!this.isActive) {
        this.$http.get("/reminders_on").then(() => {
          this.isActive = true;
          this.imgSrc =
            "https://cdn3.iconfinder.com/data/icons/communication-2-3/63/alarm-256.png";
        });
      }
    },
    onClickOff: function() {
      if (this.isActive) {
        this.$http.get("/reminders_off").then(() => {
          this.isActive = false;
          this.imgSrc =
            "https://cdn3.iconfinder.com/data/icons/communication-2-3/63/alarm-off-256.png";
        });
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
