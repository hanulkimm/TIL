<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-body-tertiary nav-sticky">
      <div class="container-fluid nav-color">
        <a class="navbar-brand" href="#">싸피사진</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" to="/movies">Movie</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/random">Random</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/watch-list">WatchList</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

.nav-sticky{
  position: sticky;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.nav-color{
  background-color: #e3f2fd;
}
</style>
