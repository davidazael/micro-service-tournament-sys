<template>
  <div class="center">
    <div>
      <img alt="Vue logo" src="../assets/logo.png" />
    </div>
    <hr />
    <div>
      {{ message }}
    </div>
    <hr />
    <div class="my-list-pos">
      <ul>
        <li v-for="u in showUsers" :key="u.node.id">
          <h6>{{ u.node.name }}</h6>
        </li>
      </ul>
    </div>
  </div>
  <hr />
  <OrgChart />
</template>

<script>
import { ref } from 'vue'
import { useQuery, useResult } from '@vue/apollo-composable'
import allUsersQuery from '../graphql/allUsers.query.gql'
import Button from 'primevue/button'
import OrgChart from '../components/OrgChart.vue'

export default {
  name: 'Test',
  components: {
    Button,
    OrgChart,
  },
  setup() {
    // data
    // method
    // computed
    // lifecycle hooks
    const handleClick = () => {
      console.log("I've been clicked.")
      // useRouter().push({ name: 'Home' })
    }

    const message = ref('Hello David!')
    const { result, error, loading } = useQuery(allUsersQuery)
    if (error) console.log('Error: ' + error.value)
    if (loading || !result) console.log('Loading: ' + loading.value)
    const showUsers = useResult(result, undefined, data => data.usersList.edges)

    return { message, showUsers, handleClick }
  },
}
</script>

<style scoped>
.my-list-pos {
  display: inline-block;
}
</style>
