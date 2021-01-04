<template>
  <div v-if="modal_is_showed" class="error-modal">
    <div class="error-close" v-on:click="close_error_modal">X</div>
    <div class="error-content">
      {{ $props.error_name }}
    </div>
  </div>
</template>

<script>
export default {
  name: "Error",
  props : [
    'error_name'
  ],
  data : function() {
    return {
      modal_is_showed : true
    }
  },
  methods : {
    close_error_modal : function() {
      this.modal_is_showed = false;
      this.$emit(
        'close_error_modal'
      )
    }
  }
}
</script>

<style scoped>
  .error-modal {
    border: 3px solid #ff6486;
    border-radius: 10px;
    padding: 5px;
    position: absolute;
    left: 50%;
    top: 20%;
    transform: translate(-50%, -50%);
    background-color: #ffb8c8;
    width: 40%;
    height: 200px;
    z-index: 20;
  }

  .error-close {
    position: relative;
    color: red;
    left: 90%;
    top: 10%;
    cursor: pointer;
  }

  .error-content {
    text-align: center;
    font-size: 25pt;
    margin-top: 25px;
  }
</style>
