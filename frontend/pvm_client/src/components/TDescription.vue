<template>
  <div class="tdesc_wrapper">
    <div class="tdesc_wrapper_close" v-on:click="$emit('tdesc_close')">X</div>
  </div>
</template>

<script>
export default {
  name: "TDescription"
}
</script>

<style scoped>
  .tdesc_wrapper {
    position: absolute;
    top: 49%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: 2px solid grey;
    background-color: #c9ffd9;
    width: 50%;
    height: 80%;
    z-index: 9999;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  }

  .tdesc_wrapper_close {
    color: red;
    position: relative;
    left: 45%;
    top: 5%;
    cursor: pointer;
  }

  @media screen and (max-width: 500px) {
    .tdesc_wrapper {
      width: 100%;
    }
  }
</style>
