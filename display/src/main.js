import { createApp, h, provide } from 'vue'
import { ApolloClient, gql, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'
import App from './App.vue'
import router from '@/router'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'
// import 'primevue/resources/themes/vela-blue/theme.css'
import 'primevue/resources/themes/saga-blue/theme.css' //theme
import 'primeicons/primeicons.css' //icons
import 'primevue/resources/primevue.min.css' //core css
import 'primeflex/primeflex.css'
import Dialog from 'primevue/dialog'

// const source = 'http://localhost/assoc/graphql'
const source = 'http://localhost/users/graphql'
// const source = 'https://rickandmortyapi.com/graphql/'

const defaultClient = new ApolloClient({
  uri: source,
  cache: new InMemoryCache(),
})

createApp({
  setup() {
    provide(DefaultApolloClient, defaultClient)
  },
  render() {
    return h(App)
  },
})
  .use(router)
  .use(PrimeVue, { ripple: true })
  .component('Dialog', Dialog)
  .use(ToastService)
  .mount('#app')
