<template>
  <div class="col">
    <div class="card">
      <img :src="imgURL" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{movie.title}}</h5>
        <p class="card-text">{{movie.overview}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'MovieCard',
  data(){
    return {
      imgURL: `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    }
  },
  props: {
    movie:Object
  }
}
</script>

<style>

</style>