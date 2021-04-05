<template>
  <div>
    <Header />
  </div>
  <div>
    <div class="p-d-flex p-p-3 card">
      <Button type="Button" icon="pi pi-check" class="p-mr-2" />
      <Button type="Button" icon="pi pi-trash" class="p-button-danger" />
      <Button
        type="Button"
        icon="pi pi-search"
        class="p-ml-auto p-button-help"
      />
    </div>
    <div class="p-d-flex p-shadow-24 p-jc-center">
      Flex Container
      <div class="p-mr-2">Item 1</div>
      <div class="p-mr-2">Item 2</div>
      <div>Item 3</div>
    </div>
    <div class="p-grid">
      <div class="p-col">1</div>
      <div class="p-col">2</div>
      <div class="p-col">3</div>
    </div>
  </div>
</template>

<script>
import Button from 'primevue/button'

export default {
  components: {
    Button,
  },
}
</script>

<style></style>
