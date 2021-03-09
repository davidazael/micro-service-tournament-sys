<template>
  <!-- <NavBar /> -->
  <div>
    <h1>This is Home</h1>
    <hr />
    <Button label="Info" @click="showInfo" />
  </div>
</template>

<script>
import { useToast } from 'primevue/usetoast'
import Button from 'primevue/button'
// import NavBar from '../components/layouts/NavBar.vue'

export default {
  components: {
    // NavBar,
    Button,
  },
  setup() {
    const toast = useToast()

    const showInfo = () => {
      toast.add({
        severity: 'info',
        summary: 'Info Message',
        detail: 'Message Content',
        life: 3000,
      })
    }

    return { showInfo }
  },
}
</script>

<style></style>
