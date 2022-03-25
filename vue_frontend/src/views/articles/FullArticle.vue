<template>
    <h1>This is an article</h1>
    <p>{{slug}}</p>
</template>

<script>
export default {
    name: "FullArticle",
    data() {
       return { slug: this.$route.params.slug }
    }
}
</script>

<style scoped>

</style>