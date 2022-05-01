<template>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name: 'home' }">Ceteris Paribus</router-link>
      <ul class="navbar-nav">
        <li class="nav-item"><router-link class="nav-link" :to="{ name: 'articles' }">Articles</router-link></li>
        <li class="nav-item"><router-link class="nav-link" :to="{ name: 'dashboards' }">Data Dashboards</router-link></li>
        <li class="nav-item"><router-link class="nav-link" :to="{ name: 'north_korea' }">North Korea</router-link></li>
        <li class="nav-item"><router-link class="nav-link" :to="{ name: 'developer_documentation' }">Developer Documentation</router-link></li>
        <li class="nav-item"><router-link class="nav-link" :to="{ name: 'about' }">About</router-link></li>
      </ul>
    </div>
  </nav>
  <router-view/>
  <div>
    <h2>This is a placeholder for the footer</h2>
  </div>
</template>

<style>
#app {
  font-family: "Times New Roman", Times, serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #292929;
  --secondary-color: #FE828C;
  --text-color: #bccadb;
}

.navbar {
  padding: 30px;
  background-color: black !important;

}
.navbar{
  height: 70px !important;
}

nav a {
  font-weight: bold;
  color: #bccadb !important;
}
.navbar-brand:hover{
  color:#FE828C !important;
}
.nav-link{
  color: #bccadb;
}
.nav-link:hover{
  color: #FE828C !important;
}
</style>



