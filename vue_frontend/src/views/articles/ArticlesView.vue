<template>
    <div class="articles">
        <ArticleCategory :category="category" v-for="(category, index) in categories" :key="index"/>
    </div>
</template>

<script>
import ArticleCategory from '@/components/articles/ArticleCategory.vue'

export default {
    name: "ArticlesIndexView",
    components: { ArticleCategory },
    data() {
        return {
            categories: [
                {name:"North Korea"},
                {name:"Economics "}
            ]
        }
    }
}
</script>

<style scoped>

</style>
