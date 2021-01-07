<template>
  <div>
    <error
      :error_name="this.error"
      v-if="this.tasks_error"
      @close_error_modal="error_close"
    >
    </error>

    <tdesc
      v-if="!tdesc_is_close"
      @tdesc_close="tdesc_close"
    >
    </tdesc>

    <div v-for="task in tasks" :key="task.N">
      <task
        :N="task.N"
        :title="task.title"
        :deadline_date="task.deadline_date"
        :deadline_time="task.deadline_time"
        :time="task.time"
        :stamp="task.stamp"
        :priority="task.priority"
        :newest="task.newest"

        @start_task="start_task"
        @stop_task="stop_task"
        @save_task="save_task"
      />
    </div>
    <div class="badge bg-success add-btn" v-on:click="add_task">+ADD</div>
  </div>
</template>

<script>
import Task from './Task.vue';
import Error from "./Error";
import TDescription from "./TDescription";

export default {
  name: "TasksView",
  components : {
    'task' : Task,
    'error' : Error,
    'tdesc' : TDescription
  },
  props: [
    'current_task'
  ],
  methods : {
    tdesc_close : function () {
      this.tdesc_is_close = true;
    },

    error_close : function() {
      this.tasks_error = false;
      this.error = '';
    },

    save_task( new_task ) {
      let new_task_indx = this.tasks.findIndex(
        (e, i, a) => {
          if ( e.N === new_task.N ) return "hello world";
          return false;
        }
      );

      this.$set(
        this.tasks,
        new_task_indx,
        Object.assign(
          {},
          this.tasks,
          new_task
        )
      );
    },

    start_task( title ) {
      this.$emit(
        'set_task',
        title
      )
    },

    stop_task( title ) {
      this.$emit(
        'stop_task',
        title
      )
    },

    add_task() {
      let task_object = {
          N : this.tasks.length > 0 ? this.tasks[ this.tasks.length - 1].N + 1 : 0,
          title : '---',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '0',
          priority : null,
          newest : true
      };

      this.$set(
        this.tasks,
        this.tasks.length,
        task_object
      );
    }
  },
  data: function () {
    return {
      tasks : null,
      tasks_error : false,
      error : '',
      tdesc_is_close : false
    }
  },
  mounted() {
    let JWT = localStorage.getItem('_jwt');
    if ( !JWT ) this.$router.push('/');
    else {
      fetch(
        process.env.baseUrl + '/tasks',
        {
          method : 'GET',
          headers : {
            'Authorization' : JWT
          }
        }
      ).then( response => response.json() )
        .then(
          ( data ) => {
            if ( data.error ) throw data.error;
            else if ( data.msg === 'Token has expired' ) {
              localStorage.clear();
              this.$router.push('/');
            } else {
              this.tasks = data.tasks;
              // emitting count of tasks to footer-component
              this.$emit(
                'tasks_count',
                this.tasks.length
              );
            }
          }
        )
      .catch(
        (error) => {
          this.tasks_error = true;
          this.error = error;
        }
      )
    }
  }
}
</script>

<style scoped>
  .tasks {
    display: block;
  }

  .tasks > div {
    border: 2px solid #828282;
    border-radius: 5px;
    padding: 5px;
    margin: 10px auto;
    width: 98%;
    height: 50px;
    cursor: pointer;
  }

  .tasks > div:hover {
    border: 2px solid goldenrod;
  }


  .add-btn {
    display: block;
    width: 50px;
    margin: 10px auto;
    cursor: pointer;
  }
</style>
