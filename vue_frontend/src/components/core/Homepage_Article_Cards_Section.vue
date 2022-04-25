<template>
<div class="articles_section">
    <h3>Recent Articles</h3>
    <div class="homepage_article_grid">
        
        <div class="article_card">
            <div class="article_card_content">
                <h4 class="article_card_title">The world population increased from 1 billion in 1800 to 7.9 billion today.</h4>
                <div class="article_info">
                    <p><strong>By</strong>: Matthew Teelucksingh</p>
                    <p><strong>Published on</strong>: 25/04/2022</p>
                </div>
                <p class="article_card_paragraph">Growth slowed from 2.2% per year 50 years ago to 1.0% per year today...</p>
                <div class="article_card_link">
                    <div><h5 class="article_topic">North Korea</h5></div>
                    <div><h5 class="article_link">Read the full article...</h5></div>                    
                </div>
            </div>
        </div>
        
        <div class="article_card">
            <div class="article_card_content">
                <h4 class="article_card_title">The world population increased from 1 billion in 1800 to 7.9 billion today.</h4>
                <div class="article_info">
                    <p><strong>By</strong>: Matthew Teelucksingh</p>
                    <p><strong>Published on</strong>: 25/04/2022</p>
                </div>
                <p class="article_card_paragraph">Growth slowed from 2.2% per year 50 years ago to 1.0% per year today...</p>
                <div class="article_card_link">
                    <div><h5 class="article_topic">North Korea</h5></div>
                    <div><h5 class="article_link">Read the full article...</h5></div>                    
                </div>
            </div>
        </div>
        
        <div class="article_card">
            <div class="article_card_content">
                <h4 class="article_card_title">The world population increased from 1 billion in 1800 to 7.9 billion today.</h4>
                <div class="article_info">
                    <p><strong>By</strong>: Matthew Teelucksingh</p>
                    <p><strong>Published on</strong>: 25/04/2022</p>
                </div>
                <p class="article_card_paragraph">Growth slowed from 2.2% per year 50 years ago to 1.0% per year today...</p>
                <div class="article_card_link">
                    <div><h5 class="article_topic">North Korea</h5></div>
                    <div><h5 class="article_link">Read the full article...</h5></div>                    
                </div>
            </div>
        </div>

        <div class="article_card">
            <div class="article_card_content">
                <h4 class="article_card_title">The world population increased from 1 billion in 1800 to 7.9 billion today.</h4>
                <div class="article_info">
                    <p><strong>By</strong>: Matthew Teelucksingh</p>
                    <p><strong>Published on</strong>: 25/04/2022</p>
                </div>
                <p class="article_card_paragraph">Growth slowed from 2.2% per year 50 years ago to 1.0% per year today...</p>
                <div class="article_card_link">
                    <div><h5 class="article_topic">North Korea</h5></div>
                    <div><h5 class="article_link">Read the full article...</h5></div>                    
                </div>
            </div>
        </div>

        <div class="article_card">
            <div class="article_card_content">
                <h4 class="article_card_title">The world population increased from 1 billion in 1800 to 7.9 billion today.</h4>
                <div class="article_info">
                    <p><strong>By</strong>: Matthew Teelucksingh</p>
                    <p><strong>Published on</strong>: 25/04/2022</p>
                </div>
                <p class="article_card_paragraph">Growth slowed from 2.2% per year 50 years ago to 1.0% per year today...</p>
                <div class="article_card_link">
                    <div><h5 class="article_topic">North Korea</h5></div>
                    <div><h5 class="article_link">Read the full article...</h5></div>                    
                </div>
            </div>
        </div>


    </div>
</div>
</template>

<script>
export default{
    name: "HomepageArticleCards"
}
</script>

<style scoped>
.articles_section{
    padding-top: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}
.articles_section h3{
    color: var(--secondary-color);
    text-align: left;
}
.homepage_article_grid{
    display: grid;
    gap: 0.5rem;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
}
.article_card{
    border: solid 1px;
}
.article_card_title{
    color: #92092c;;
}
.article_card_content{
    background-color: #bccadb7a;
    padding: 1.5rem; 
    color: black;
    text-align: left;
    
}
.article_info p{
    margin-bottom: 0;
    font-size: 0.9rem; 
}
.article_card_paragraph{
    font-size: 1.0rem;
    margin-top: 0.75rem;
}
.article_card_link h5{
    font-size: 1rem;
}
.article_card_link{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(11rem, 1fr));
}
</style>