<template>
    <div class="main_category">
        <h2 id="category_title">{{category.name}}</h2>
        <div class="article_category_grid">
            <ArticlePreview :article_preview="article_preview" v-for="(article_preview, index) in test_blog_posts" :key="index"/>
        </div>
        <h3><router-link class="category_link" :to="{ name: 'home' }">Show More....</router-link></h3>

    </div>
  
</template>

<script>
// Importing single Article Preview Component:
import ArticlePreview from "@/components/articles/ArticlePreview.vue"

export default {
    name: "ArticleCategory",
    components: {ArticlePreview},
    props: ["category"],

    data() {
        return {
            
            // Given a category provided it queries article summaries based on specified category:
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
                {
                    title: "This is the title of Article 3",
                    summary: "A test summary for the article 3",
                    author: "Matthew Teelucksingh",
                    slug: "this-is-the-title-of-article-3"
                },
                {
                    title: "This is the title of Article 3",
                    summary: "A test summary for the article 3",
                    author: "Matthew Teelucksingh",
                    slug: "this-is-the-title-of-article-3"
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

    .main_category{
        padding-left: 5%;
        padding-right: 5%;
    }

    #category_title{
        text-align: left;
        padding-top: 1rem;
    }

    .article_category_grid{
        display: grid;
        column-gap: 1rem;
        row-gap: 1rem;
        grid-template-columns: repeat(3, 1fr);
    }
    
    .category_link{
        text-align: center;
        color: black;
    }
</style>