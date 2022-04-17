<template>
  <div class="article_summary_card">
      <h3 class="article_title">{{article_preview.title}}</h3>
      <p class="article_summary">{{article_preview.summary}}</p>
      <router-link :to="{ name: 'FullArticle', params:{slug:article_preview.slug}}">Test Link</router-link>
  </div>
</template>

<script>
export default {
    name: "ArticlePreview",
    props: ["article_preview"]
}
</script>

<style scoped>
  /* Creating the main object for wrapping the article card: */
  .article_summary_card{
    padding: 0.8rem;
    border-style: solid;
    border-width: medium;
  }

</style>

