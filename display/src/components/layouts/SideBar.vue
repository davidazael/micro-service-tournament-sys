<template>
  <div class="main-menu">
    <Sidebar v-model:visible="visibleLeft" class="p-sidebar-sm">
      <div class="p-d-flex" v-for="r in allRoutes" :key="r.name">
        <div class="p-m-0 p-jc-md-evenly">
          <Button class="p-button-outlined"> {{ r.name }} </Button>
        </div>
      </div>
    </Sidebar>
    <Button icon="pi pi-arrow-right" @click="visibleLeft = true" />
  </div>
</template>

<script>
import Divider from 'primevue/divider'
import Listbox from 'primevue/listbox'
import SelectButton from 'primevue/selectbutton'
import MegaMenu from 'primevue/megamenu'
import { ref } from 'vue'
import Sidebar from 'primevue/sidebar'
import Button from 'primevue/button'
import { useRouter } from 'vue-router'

export default {
  components: {
    Divider,
    Listbox,
    SelectButton,
    Sidebar,
    Button,
    MegaMenu,
  },
  setup() {
    const visibleLeft = ref(false)
    const visibleRight = ref(false)
    const router = useRouter()

    // const allRoutes = ['root', 'about', 'helloworld', 'test']
    const allRoutes = router.getRoutes().filter(x => x.name !== undefined)

    const currRoute = router.currentRoute.value.name

    console.log(allRoutes)
    console.log(currRoute)
    console.log(router.currentRoute)

    function goTo(path) {
      router.push(path)
    }

    const selected = null

    return {
      currRoute,
      selected,
      goTo,
      allRoutes,
      visibleRight,
      visibleLeft,
    }
  },
}
</script>

<style>
.main-menu {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>
