<template>
  <div>
    <div class="header">
      <div v-if="time_is_loading">
        ⌛
      </div>
      <div v-else class="badge" v-bind:class="{ 'bg-danger' : current_status === 'FAIL', 'bg-success' : current_status === 'OK' }">
        {{ current_status }}
      </div>
      <div v-if="current_task.length > 0 && current_status === 'OK'" style="color: white">
        {{ current_task[0] }}
      </div>
    </div>

    <div v-if="current_status !== 'FAIL'" class="workflow">
      <tasks
        @set_task="set_task"
        @stop_task="unset_task"
        @tasks_count="set_summary"
      >
      </tasks>
    </div>
    <div v-else>
      <div class="backend-error">
        Backend is not responding! =(
      </div>
    </div>
    <vfooter
      :summary="this.footer_summary"
    >
    </vfooter>
  </div>
</template>

<script>
import Tasks from "./Tasks.vue"
import Footer from "./Footer.vue"

export default {
  name: "Main",
  time : null,
  components : {
    'tasks' : Tasks,
    'vfooter' : Footer
  },
  methods: {
    unset_task : function( title ) {
      this.current_task.splice(
        this.current_task.indexOf(title),
        1
      );
    },

    set_task : function( title ) {
      this.current_task.splice(
        0,
        0,
        title
      );
    },

    set_summary : function( count ) {
      this.footer_summary = count;
    }
  },

  data: function () {
    return {
      current_status : null,
      time_is_loading : true,
      current_task : [],

      footer_summary : null
    }
  },

  mounted() {
    this.time = setInterval(
      () => {
              fetch(
          process.env.baseUrl + "/time"
              ).then(
                response => response.json()
              ).then(
                ( data ) => {
                  this.current_status = "OK";
                  this.time_is_loading = false;
                }
              ).catch(
                () => {
                  this.current_status = "FAIL";
                }
              )
      },
      5000
    )
  },

  destroyed() {
    clearInterval( this.time );
  }
}
</script>

<style scoped>
  .header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    background-color: black;
    width: 100%;
    height: 10%;
    padding: 5px;
    text-align: center;
  }

  .workflow {
    width: 100%;
    height: 100%;
    display: block;
    text-align: center;
  }

  .backend-error {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 18pt;
    color: red;
  }
</style>
