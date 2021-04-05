<template>
  <Toast />
  <NavBar />
</template>

<script>
import NavBar from './components/layouts/NavBar.vue'
import Toast from 'primevue/toast'
import { useRouter } from 'vue-router'
import Button from 'primevue/button'

export default {
  name: 'App',
  components: {
    NavBar,
    Button,
    Toast,
  },
  setup() {
    const router = useRouter()

    // const allRoutes = ['root', 'about', 'helloworld', 'test']
    const allRoutes = router.getRoutes().filter(x => x.name !== undefined)

    function goTo(path) {
      router.push(path)
    }

    return {
      goTo,
      allRoutes,
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
