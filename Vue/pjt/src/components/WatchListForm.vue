<template>
  <form @submit.prevent="AddWatchList"> 
    <h2>보고싶은 영화</h2>
    <input type="text" name="movie" id="movie" v-model="movie">
    <button type="submit">Add</button>
  </form>
</template>

<script>
export default {
  name:'WatchListForm',
  data(){
    return {
      movie:null,
    }
  },
  methods:{
    AddWatchList(){
      const movie = this.movie
      this.$store.dispatch('AddWatchList', movie)
      this.movie = ''
    }    
  }
}
</script>

<style>

</style>