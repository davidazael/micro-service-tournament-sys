<template>
  <div class="p-grid">
    <div id="1" class="p-col">1</div>
    <div id="2" class="p-col">{{ colTwo }}</div>
    <div class="p-col">3</div>
  </div>
</template>

<script>
export default {
  props: ['colTwo'],
}
</script>

<style></style>
