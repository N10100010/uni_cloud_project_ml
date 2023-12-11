import { createRouter, createWebHistory } from 'vue-router'
import Start from '../components/Start.vue'
import Load from '../components/Load.vue'
import sb from '../components/tiles/searchBar.vue'
import ModelUse from '../components/ModelUse.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: Start,
    },
    {
      path: '/load',
      name: 'load',
      component: Load
    },
    {
      path: '/sb',
      name: 'sb',
      component: sb
    },
    {
        path: '/model-use/:modelId',
        name: 'ModelUse',
        component: ModelUse,
        props: true,
    },
  ]
})

export default router
