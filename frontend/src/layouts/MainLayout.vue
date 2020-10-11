<template>
  <div class="container">
    <img class="logo" alt="Vue logo" src="../assets/logo.png">
    <ul>
      <li>
        <router-link to="/">Home</router-link>
      </li>
      <li>
        <router-link to="/characters">Character list</router-link>
      </li>
    </ul>
    <slot></slot>
  </div>
</template>

<script>

export default {}
</script>

<style lang="scss">
@import "../assets/style";
</style>