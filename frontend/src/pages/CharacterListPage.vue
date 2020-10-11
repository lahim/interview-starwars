<template>
  <main-layout>
    <h3>Character list</h3>
    <CharacterList/>
  </main-layout>
</template>

<script>
import MainLayout from "@/layouts/MainLayout";
import CharacterList from "@/components/CharacterList";

export default {
  name: 'CharacterDetailPage',
  components: {
    MainLayout,
    CharacterList
  }
}
</script>
<style>
</style>
