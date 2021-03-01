import { createApp, h, provide } from 'vue'
import { ApolloClient, gql, InMemoryCache } from '@apollo/client/core'
import { DefaultApolloClient } from '@vue/apollo-composable'
import App from './App.vue'

// const source = 'http://localhost/assoc/graphql'
const source = 'http://localhost/users/graphql'
// const source = 'https://rickandmortyapi.com/graphql/'

const defaultClient = new ApolloClient({
  uri: source,
  cache: new InMemoryCache(),
})

// const query = gql`
//   query UsersList {
//     usersList {
//       edges {
//         node {
//           id
//           name
//         }
//       }
//     }
//   }
// `

// const query = gql`
//   query {
//     characters {
//       results {
//         name
//       }
//     }
//   }
// `

// defaultClient
//   .query({
//     query,
//   })
//   .then(res => console.log(res))

createApp({
  setup() {
    provide(DefaultApolloClient, defaultClient)
  },
  render() {
    return h(App)
  },
}).mount('#app')
