<template>
  <div>
    <WatchListForm/>
    <WatchListItem v-for="movie in watchList" :key="`${movie}`" :movie="movie"/>
  </div>
</template>

<script>
import WatchListForm from '../components/WatchListForm'
import WatchListItem from '../components/WatchListItem.vue'
export default {
  name:'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed:{
    watchList(){
      return this.$store.state.watchList
    },
  },
  created(){
    this.$store.state.watchList = localStorage.getItem('watchList')?JSON.parse(localStorage.getItem('watchList')):[]
  
  }

}
</script>

<style>

</style>