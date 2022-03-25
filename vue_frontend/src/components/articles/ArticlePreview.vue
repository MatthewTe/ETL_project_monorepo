<template>
  <div class="article_preview_main">
      <h1>{{article_preview.title}}</h1>
      <p>{{article_preview.summary}}</p>
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

</style>

