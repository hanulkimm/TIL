import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const apikey = process.env.VUE_APP_TMDB_API_KEY
const movieURL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${apikey}&language=ko&region=KR`


export default new Vuex.Store({
  state: {
    movies:[],
    watchList : [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movieList){
      state.movies = movieList
    },
    ADD_WATCH_LIST(state, movie){
      const isActive = false
      state.watchList.push({movie, isActive})
      const stringifyList = JSON.stringify(state.watchList)
      localStorage.setItem('watchList',stringifyList)
    },
    WATCH_TOGGLE(state, movie){
      movie.isActive = !movie.isActive
      const stringifyList = JSON.stringify(state.watchList)
      localStorage.setItem('watchList',stringifyList)
    }
  },
  actions: {
    getMovies(content){
      axios({
        method:'get',
        url: movieURL,
      })
      .then((res)=>{
        const movieList = res.data.results
        content.commit('GET_MOVIES', movieList)
      })
      .catch((err)=>{
        console.log(err)
        console.log(apikey)
      })
    },
    AddWatchList(content, payload){
      if (content.state.watchList.every(element => {
        return element['movie'] !== payload
      })){
        console.log(content.state.watchList)
        content.commit('ADD_WATCH_LIST', payload)
      }
    },
    watchToggle(content, movie){
      content.commit('WATCH_TOGGLE', movie)
    }
  },
  modules: {
  }
})
