<template>
  <div class="task_info"
       v-bind:class="{
        'task_pri_null' : $props.priority == null,
        'task_pri_high' : $props.priority == 1,
        'task_pri_medium' : $props.priority == 0,
        'task_pri_low' : $props.priority == -1
       }"
  >
    <template v-if="$props.newest">
      <div>
        <input type="text" :style="{ borderColor: new_task.title ? '' : 'red' }" placeholder="Task title" v-model="new_task.title" />
      </div>
      <div v-if="$props.newest === true">
        priority:<br>
        Low: <input type="radio" :name="$props.id + '_priority'" v-model="new_task.priority" value="-1" checked/>
        Middle: <input type="radio" :name="$props.id + '_priority'" v-model="new_task.priority" value="0" />
        High: <input type="radio" :name="$props.id + '_priority'" v-model="new_task.priority" value="1">
      </div>
      <div>
        <button type="button" class="button-save" :disabled="!( new_task.title && new_task.deadline_date && new_task.deadline_time )" v-on:click="save">SAVE</button>
      </div>

      <div>
        <input type="date" placeholder="Deadline date" v-model="new_task.deadline_date" :min="today_date" />
        <br>
        <input type="time" placeholder="Deadline time" v-model="new_task.deadline_time" :min="today_time"/>
      </div>
    </template>
    <template v-else>
      <div class="task_title">
        {{ $props.title }}
      </div>
      <div class="task_bar">
        <span class="task_bar_play"
              v-bind:class="{ 'sepia_filter' : is_play_enable }"
              v-on:click="play( $props.title )"
        >▶</span>
        <span class="task_bar_stop"
              v-bind:class="{ 'sepia_filter' : !is_play_enable }"
              v-on:click="stop"
        >⏸</span>
      </div>

      <div class="task_time_format">
        {{ fancyTimeFormat( this.task_stamp ) }}
      </div>
      <div class="task_time">
        <div
          class="task_progress"
          v-bind:style="{
            width: (this.task_stamp / $props.time) * 100 + '%'
          }"
        >
        </div>
      </div>

      <div class="task_title" style="text-align: center">
        {{ this.deadline_date }}
        <br>
        {{ this.deadline_time }}
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: "Task",
  props: [
    'id',
    'title',
    'deadline_date',
    'deadline_time',
    'stamp',
    'time',
    'priority',
    'newest'
  ],

  methods : {
    save: function() {
      console.log( this.new_task.priority );
      this.$emit(
        'save_task',
        this.new_task
      )
    },
    play : function( title ) {
      this.is_play_enable = true;
      this.task_timer = setInterval(
        () => {
          this.task_stamp = "" + ( parseInt(this.task_stamp) + 1 );
        },
        1000
      );
      this.$emit(
        'start_task',
        title
      )
    },
    stop : function() {
      this.is_play_enable = false;
      if ( this.task_timer ) clearInterval( this.task_timer )
    },

    // shomrat
    fancyTimeFormat : function(duration) {
      let hrs = ~~(duration / 3600);
      let mins = ~~((duration % 3600) / 60);
      let secs = ~~duration % 60;
      let ret = "";

      if (hrs > 0) {
          ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
      }

      ret += "" + mins + ":" + (secs < 10 ? "0" : "");
      ret += "" + secs;
      return ret;
    }
  },

  data: function() {
    return {
      new_task : {
        id : this.id,
        title : null,
        priority : -1,
        deadline_date: "1997-09-19",
        deadline_time: "10:30",
        newest : false
      },

      is_play_enable : false,
      task_timer : null,
      task_stamp : this.stamp,

      today_date : new Date().toJSON().split('T')[0],
      today_time : new Date().toJSON().split('T')[1],
    }
  },
}
</script>

<style scoped>
  input {
    border-radius: 5px;
    text-align: center;
  }

  button {
    border-radius: 5px;
  }

  .button-save {
    background-color: aquamarine;
  }

  .task_pri_null {
    background-color: #ffffff;
    border: 2px dashed grey !important;
  }

  .task_pri_high {
    background-color: #ff6486;
  }

  .task_pri_medium {
    background-color: #ffcb64;
  }

  .task_pri_low {
    background-color: #74ff64;
  }

  .sepia_filter {
    filter: sepia( 100 );
  }

  .task_progress {
    width: 0;
    background-color: darkslategrey;
    height: 15px;
    font-size: 8pt;
  }

  .task_time {
    width: 40%;
    border: 1px solid black;
    border-radius: 5px;
  }

  .task_info {
    width: 99%;
    margin: 10px auto;
    padding: 5px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    align-items: center;
    border: 2px solid #828282;
    border-radius: 5px;
    cursor: pointer;
  }

  .task_title {
    text-align: left;
    font-size: 9pt;
  }
</style>
