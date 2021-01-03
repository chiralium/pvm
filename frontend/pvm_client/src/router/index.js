import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/tasks',
      name: 'Main',
      component: Main
    },
    {
      path: '/',
      name: 'Login',
      component: Login
    }
  ]
})
