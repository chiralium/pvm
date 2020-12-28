<template>
  <div>
    <div v-for="task in tasks" :key="task.title">
      <task
        :title="task.title"
        :deadline_date="task.deadline_date"
        :deadline_time="task.deadline_time"
        :time="task.time"
        :stamp="task.stamp"
        :priority="task.priority"
        @start_task="start_task"
      />
    </div>
    <div class="badge bg-success add-btn">+ADD</div>
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
    start_task( title ) {
      this.$emit(
        'set_task',
        title
      )
    }
  },
  data: function () {
    return {
      tasks : [
        {
          title : 'Test task #1',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '0',
          priority : 1,
        },
        {
          title : 'Test task #2',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '50',
          priority : 0,
        },
        {
          title : 'Test task #3',
          deadline_date : '30.12.2020',
          deadline_time : '00:00',
          time : '6000',
          stamp : '360',
          priority : -1,
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
