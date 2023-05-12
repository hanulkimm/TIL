<template>
  <div>
    <p :class="{isActive:movie.isActive}" @click="watchToggle">{{movie.movie}}</p>
    
  </div>
</template>

<script>
export default {
  name:'WatchListItem',
  props:{
    movie: Object,
  },
  methods:{
    watchToggle(){
      this.$store.dispatch('watchToggle', this.movie)
    }
  },
}
</script>

<style>
.isActive{
  text-decoration: line-through;
}
</style>