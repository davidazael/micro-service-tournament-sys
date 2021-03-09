<template>
  <div>
    <TabMenu :model="items" />
    <router-view />
    <h1>Hello From TabMenu</h1>
  </div>
</template>

<script>
import TabMenu from 'primevue/tabmenu'

export default {
  components: {
    TabMenu,
  },
  data() {
    return {
      items: [
        { label: 'App', icon: 'pi pi-fw pi-home', to: '/' },
        { label: 'HelloWorld', icon: 'pi pi-fw pi-home', to: '/helloworld' },
      ],
    }
  },
}
</script>

<style></style>
