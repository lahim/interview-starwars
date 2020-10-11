<template>
  <div class="person-list">
    <section v-if="errored">
      <p>We're sorry, we're not able to retrieve this information at the moment, please try back later.</p>
    </section>

    <!--    add fetch button -->

    <section v-else>
      <div v-if="loading">
        <p>Loading...</p>
      </div>

      <div v-else>
        <b-button v-on:click="fetchData()">Fetch data</b-button>
        <div class="alerts">
          <b-alert show dismissible v-if="message">{{ message }}</b-alert>
        </div>
        <div
            v-for="character in characters"
            :key="character.id"
            class="character"
        >
          <div class="item">
            <router-link :to="'/characters/' + character.id">
              {{ character.created_date | moment("MMMM Do YYYY, h:mm:ss a") }}
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CharacterList',
  props: {
    msg: String
  },
  data() {
    return {
      characters: null,
      loading: true,
      errored: false,
      message: null
    }
  },
  mounted() {
    this.loadCharacters()
  },
  methods: {
    loadCharacters() {
      axios
          .get('http://localhost:8000/api/characters/')
          .then(response => {
            this.characters = response.data
            console.log(this.characters)
          })
          .catch(error => {
            console.log(error)
            this.errored = true
          })
          .finally(() => this.loading = false)
    },
    fetchData() {
      this.message = 'Fetching data...'
      axios.get('http://localhost:8000/api/fetch-data/') // should be a POST method
          .then(response => {
            console.log(response.data)
            this.message = 'Data was loaded successfully.'
            this.loadCharacters()
          })
          .catch(error => {
            console.error(error)
            this.message = 'Oops! Something went wrong.'
          })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import "../assets/variables";

h1 {
  font-weight: lighter;
  font-size: large;
  color: $blue-color;
}

.alerts {
  padding: 30px 30px;
}
.character {
  font-weight: bolder;
  text-align: left;

  .item {
    padding: 6px;
  }
}
</style>
