<template>
  <div>
    <TabMenu :model="items">
      <li
        class="p-tabmenuitem"
        role="tab"
        aria-selected="false"
        aria-expanded="false"
      >
        <span>
          Search
        </span>
      </li>
    </TabMenu>
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

    console.log(allRoutes)

    console.log(allRoutes[4].props.default.icon)
    const currRoute = router.currentRoute.value.name

    allRoutes.forEach(x =>
      items.push(newItem(x.name, x.path, x.props.default.icon))
    )

    // console.log(items)

    return { items }
  },
}

function newItem(label, loc, defaultIcon = 'pi pi-fw pi-question-circle') {
  // const defaultIcon = 'pi pi-fw pi-home'
  return { label: label, icon: defaultIcon, to: loc }
}
</script>

<style scoped lang="scss">
::v-deep(.p-tabmenu) {
  ul {
    display: flex;
    justify-content: center;
  }
}
</style>
