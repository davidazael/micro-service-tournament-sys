import { createRouter, createWebHistory } from 'vue-router'

const Test = import('@/views/Test.vue')
const Default = import('@/components/DefaultLayout.vue')
const NotFound = import('@/views/NotFound.vue')

const routes = [
  {
    path: '/',
    name: 'Home',
    props: { icon: 'pi pi-home' },
    component: import('@/views/Home.vue'),
  },
  {
    path: '/helloworld',
    name: 'HelloWorld',
    component: import('@/components/HelloWorld.vue'),
  },
  {
    path: '/test',
    name: 'Test',
    props: { icon: 'pi pi-chart-bar' },
    component: Test,
  },
  {
    path: '/default',
    name: 'Default',
    component: Default,
  },
  {
    path: '/tournaments',
    name: 'Tournaments',
    props: { icon: 'pi pi-sitemap' },
    component: import('@/views/Tournaments.vue'),
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
