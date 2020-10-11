<template>
  <main-layout>
    <h3>Character detail</h3>
    <CharacterDetail />
  </main-layout>
</template>

<script>
import MainLayout from "@/layouts/MainLayout";
import CharacterDetail from "@/components/CharacterDetail";

export default {
  name: 'CharacterListPage',
  components: {
    MainLayout,
    CharacterDetail
  }
}
</script>

<style>
</style>
