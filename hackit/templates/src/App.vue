<template>
  <div id="app" class="container mt-3">
    <div class="row">
      <div class="col ml-5">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Clemson_University_Tiger_Paw_logo.svg/1200px-Clemson_University_Tiger_Paw_logo.svg.png" height="130px">
      </div>
      <div class="col"></div>
      <div class="col"></div>
      <div class="col">
        <img src="http://cuhack.it/resources/RGB_logo.png" height="130px" alt="CU-Hackit_logo">
      </div>
    </div>

    <div class="container-fluid">
      <div class="d-flex mt-5 justify-content-center">
        <h1>Reminders are: </h1>
      </div>
      <div class="d-flex justify-content-center">
        <Main/>
      </div>
    </div>

  </div>
</template>

<script>
import Main from "./components/Main.vue";

export default {
  name: "app",
  components: {
    Main
  }
};
</script>

<style>
html body {
  background-color: rgb(65, 58, 58);
  color: white;
}
</style>
