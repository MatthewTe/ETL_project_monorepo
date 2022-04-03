<template>
  <nav>
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <router-link :to="{ name: 'articles' }">Articles</router-link> |
    <router-link :to="{ name: 'dashboards' }">Data Dashboards</router-link> |
    <router-link :to="{ name: 'north_korea' }">North Korea</router-link> |
    <router-link :to="{ name: 'developer_documentation' }">Developer Documentation</router-link> |
    <router-link :to="{ name: 'about' }">About</router-link>
  </nav>
  <router-view/>
  <div>
    <h2>This is a placeholder for the footer</h2>
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

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

body {
}
</style>
