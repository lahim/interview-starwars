<template>
  <div>
    <b-table responsive :items="items"></b-table>
  </div>
</template>

<script>
export default {
  props: {
    items: null
  }
}
</script>