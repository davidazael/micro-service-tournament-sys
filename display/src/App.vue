<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Welcome to Your Vue.js App" />
  {{ message }}
  <ul>
    <li v-for="u in showUsers" :key="u.node.id">
      <h6>{{ u.node.name }}</h6>
    </li>
  </ul>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue'
import { useQuery, useResult, useMutation } from '@vue/apollo-composable'
// import allCharactersQuery from './graphql/allCharacters.query.gql'
import allUsersQuery from './graphql/allUsers.query.gql'
// import allTournamentsQuery from './graphql/allTournaments.query.gql'
// import UserByIdQuery from './graphql/UserById.query.gql'

export default {
  name: 'App',
  components: {
    HelloWorld,
  },
  setup() {
    const message = ref('Hello David!')
    const { result, error, loading } = useQuery(allUsersQuery)
    // const { getUser } = useQuery(UserByIdQuery)
    // const { getTournaments } = useQuery(allTournamentsQuery)
    if (error) console.log('Error: ' + error.value)
    if (loading || !result) console.log('Loading: ' + loading.value)
    const showUsers = useResult(result, undefined, data => data.usersList.edges)
    // const showTournaments = useResult( getTournaments, null, data => data.tournamentList)
    /*const showCharacters = useResult( result, null, data => data.characters.results)*/

    return { message, showUsers }
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
