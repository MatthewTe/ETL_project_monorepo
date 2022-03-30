<template>
    <div class="articles">
        <ArticlePreview :article_preview="article_preview" v-for="(article_preview, index) in test_blog_posts" :key="index" />
    </div>
</template>

<script>
import ArticlePreview from '@/components/articles/ArticlePreview.vue'

export default {
    name: "ArticlesIndexView",
    components: { ArticlePreview },
    data() {
        return {
            test_blog_posts: [
                {
                    title: "This is the title of Article 1",
                    summary: "A test summary for the article 1",
                    author: "Matthew Teelucksingh",
                    slug: "this-is-the-title-of-article-1"

                },
                {
                    title: "This is the title of Article 2",
                    summary: "A test summary for the article 2",
                    author: "Matthew Teelucksingh",
                    slug: "this-is-the-title-of-article-2"
                },
                {
                    title: "This is the title of Article 3",
                    summary: "A test summary for the article 3",
                    author: "Matthew Teelucksingh",
                    slug: "this-is-the-title-of-article-3"
                },
            ]
        }
    }
}
</script>

<style scoped>

</style>
