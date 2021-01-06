<template>
  <div class="footer">
    <div class="footer-container">
      <div v-if="$props.summary">Summary: {{ $props.summary }} </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  props: [
    'summary'
  ]
}
</script>

<style scoped>
  .footer-container {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    justify-content: space-around;
    color: red;
    align-content: center;
  }

  .footer {
    position: absolute;
    width: 100%;
    height: 50px;
    background-color: black;
    bottom: 0;
  }
</style>
