<template>
  <div class="homepage_masthead">
    <h1>Explore our data, analysis, research and opinions.</h1>
    <p>Open source data dashboards, articles and APIs about international economics, international relations and foregin policy</p>
  
  <div class="homepage_masthead_button_grid">
    <div class="masthead_button"><router-link :to="{ name: 'dashboards' }">Econ, Defense and Foreign Policy Dashboards</router-link></div>
    <div class="masthead_button"><router-link :to="{ name: 'articles' }">Our Opinions and Research</router-link></div>
    <div class="masthead_button"><router-link :to="{ name: 'developer_documentation' }">Get Public API Access</router-link></div>
  </div>

  </div>
</template>

<script>

export default {
  name: 'HomepageMasthead',
}
</script>

<style scoped>
.homepage_masthead{
  background: url("@/assets/core/masthead_background_transparent.png") 50% 0;
  background-size: cover;
  padding-bottom: 3rem;
  padding-top: 3rem;
}

.homepage_masthead h1 {
  font-size: 1.875rem;
  font-weight: 700;
  line-height: 1.4;
  margin: 0 auto 1.5rem;
  max-width: 39.5rem; 
  text-align: center;
  color: var(--secondary-color);
  word-wrap: break-word;
  padding-top: 1.5rem;
}
.homepage_masthead p {
  color: #bccadb;
  font-size: 1.125rem;
  font-weight: 700;
  max-width: 39.5rem; 
  line-height:  1.3;
  margin: 0 auto 1.5rem;
  text-align: center;
  word-wrap: break-word;
}

.homepage_masthead_button_grid{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
.masthead_button{
  font-size: 1.125rem;
  font-weight: 700;
  margin-top: 2.5rem;
  margin-bottom: 1rem;
}
.masthead_button a {
  color: var(--secondary-color); 
  border: 3px solid;
  padding: .35rem .7rem;
  text-decoration: none
}
</style>
