<template>
  <div>
    <div class="d-flex justify-content-center" v-if="movie">
      <div class="card" style="width: 18rem;">
        <img :src="imgURL" class="card-img-top" alt="...">
        <div class="card-body">
          <p class="card-text">{{movie.title}}</p>
        </div>
      </div>
    </div>
    <button @click="RandomMovie" class="btn btn-success dksrnlcksgdk">PICK</button>
  </div>
</template>

<script>
export default {
  name: 'RandomView',
  data(){
    return {
      movie: null,
    }
  },
  computed:{
      imgURL(){
        return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      } 
  },
  methods: {
    RandomMovie(){
      const randomIdx = Math.floor(Math.random() * this.$store.state.movies.length)
      this.movie = this.$store.state.movies[randomIdx]
    }
  },
  created(){
    this.$store.dispatch('getMovies')
  }
}
</script>

<style>
.dksrnlcksgdk{
  width: 18rem;
}
</style>