<template>
  <div>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<script>
import TabMenu from 'primevue/tabmenu'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

export default {
  components: {
    TabMenu,
  },
  setup() {
    const selected = null
    const router = useRouter()
    const items = []
    const allRoutes = router.getRoutes().filter(x => x.name !== undefined)

    const currRoute = router.currentRoute.value.name

    allRoutes.forEach(x => items.push(newItem(x.name, x.path)))

    console.log(items)

    return { items }
  },
}

function newItem(label, loc) {
  const defaultIcon = 'pi pi-fw pi-home'
  return { label: label, icon: defaultIcon, to: loc }
}
</script>

<style></style>
