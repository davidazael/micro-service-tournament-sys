<template>
  <div>
    <h1>This is Tournament Page</h1>
    <TournamentColumns col-two="message" />
  </div>
</template>

<script>
import { ref } from 'vue'
import TournamentColumns from '../components/layouts/TournamentColumns.vue'

export default {
  components: {
    TournamentColumns,
  },
  setup() {
    const message = ref('for column 2')

    return {
      message,
    }
  },
}
</script>

<style></style>
