import { createRouter, createWebHistory } from 'vue-router'

const Home = import('@/views/Home.vue')
const HelloWorld = import('@/components/HelloWorld.vue')
const Test = import('@/views/Test.vue')
const NotFound = import('@/views/NotFound.vue')
const Default = import('@/components/DefaultLayout.vue')

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/helloworld',
    name: 'HelloWorld',
    component: HelloWorld,
  },
  {
    path: '/test',
    name: 'Test',
    component: Test,
  },
  {
    path: '/default',
    name: 'Default',
    component: Default,
  },
  {
    path: '/:catchAll(.*)',
    component: NotFound,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
