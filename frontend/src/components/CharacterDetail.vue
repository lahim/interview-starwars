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
        <div class="headers">
          <div class="header">{{ character.created_date | moment("MMMM Do YYYY, h:mm:ss a") }}</div>
          <div class="header"><a v-bind:href="character.source_file">{{ character.name }}.csv</a></div>
        </div>
        <div class="columns">
          <b-badge
              v-for="col in character.table.columns" :key="col"
              v-on:click="selectColumn(col)"
              v-bind:class="{ selected: columns.indexOf(col) >= 0}"
          >{{ col }}
          </b-badge>
        </div>
        <CharactersTable v-bind:items="character.table.items"/>
        <b-button v-on:click="loadMore()">Load more</b-button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import CharactersTable from '@/components/CharactersTable';

export default {
  name: 'CharacterDetail',
  components: {
    CharactersTable
  },
  props: {
    msg: String
  },
  data() {
    return {
      character: null,
      loading: true,
      errored: false,
      offset: 10,
      columns: [],
      countData: false
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    loadMore() {
      this.offset += 10;
      this.loadData()
    },
    loadData() {
      let url = 'http://localhost:8000/api/characters/' + this.$route.params.id + '?offset=' + this.offset
      if (this.countData) {
        url += '&columns=' + this.columns.join(',')
      }
      axios
          .get(url)
          .then(response => {
            this.character = response.data
            console.log(this.character)
          })
          .catch(error => {
            console.error(error)
            this.errored = true
            this.offset = 10
          })
          .finally(() => this.loading = false)
    },
    selectColumn(col) {
      const item = this.columns.find(c => c === col)
      if (item) {
        this.columns.splice(this.columns.indexOf(item), 1)
      } else {
        this.columns.push(col)
      }
    }
  },
  watch: {
    columns(val) {
      this.countData = val.length > 1;
      this.loadData()
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

.character {
  font-weight: bolder;

  .headers {
    text-align: left;

    .header {
      font-weight: normal;
      font-size: small;
    }
  }
}

.columns {
  margin: 20px 20px;

  span {
    margin-right: 16px;
    cursor: pointer;
  }
}

.selected {
  background: $blue-color;
}
</style>
