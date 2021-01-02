<template>
  <div>
    <div v-for="task in tasks" :key="task.id">
      <task
        :id="task.id"
        :title="task.title"
        :deadline_date="task.deadline_date"
        :deadline_time="task.deadline_time"
        :time="task.time"
        :stamp="task.stamp"
        :priority="task.priority"
        :newest="task.newest"

        @start_task="start_task"
        @save_task="save_task"
      />
    </div>
    <div class="badge bg-success add-btn" v-on:click="add_task">+ADD</div>
  </div>
</template>

<script>
import Task from './Task.vue';
export default {
  name: "TasksView",
  components : {
    'task' : Task
  },
  props: [
    'current_task'
  ],
  methods : {
    save_task( new_task ) {
      let new_task_indx = this.tasks.findIndex(
        (e, i, a) => {
          if ( e.id === new_task.id ) return "hello world";
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
    add_task() {
      let task_object = {
          id : this.tasks[ this.tasks.length - 1].id + 1,
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
      tasks : [
        {
          id : 0,
          title : 'Test task #1',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '0',
          priority : 1,
          newest : false
        },
        {
          id : 1,
          title : 'Test task #2',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '50',
          priority : 0,
          newest : false
        },
        {
          id : 2,
          title : 'Test task #3',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '360',
          priority : -1,
          newest : false
        },
      ]
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
