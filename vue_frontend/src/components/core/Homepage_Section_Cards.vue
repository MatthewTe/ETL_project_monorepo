<template>
    <div class="homepage_section_cards">
        <div class="main_section_card_grid">
            <div class="main_section_card">
                <div class="card_image"><img src="@/assets/core/Checkpoin_Charlie_image.jpg" alt=""></div>
                <div class="card_content">
                    <h4>Articles and opinions</h4>
                    <p>Ceteris paribus publishes various writings ranging from formal articles and whitepapers about our data collection and dashboards to fully opinionated articles by authors discussing contemporary issues mainly in the fields of international economics and foregin policy (or geopolitics depending on where you’re from).</p>
                </div>
                
            </div>

            <div class="main_section_card">
                <div class="card_image"><img src="@/assets/core/korean_main_thumbnail.jpeg" alt=""></div>
                <div class="card_content">
                    <h4>The Korean-Peninsula and its unique issues and international position</h4>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium facilis earum velit nobis deserunt. Reprehenderit beatae molestiae deserunt id, quia error itaque, esse quaerat rerum dolores minus ad odit necessitatibus.</p>
                </div>
            </div>

            <div class="main_section_card">
                <div class="card_image">
                    <img src="@/assets/core/Data_API_Screenshot.png" alt=""></div>
                <div class="card_content">
                    <h4>See documentation for how to use our public data APIs</h4>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae odit quod eos praesentium doloribus quaerat aliquam blanditiis voluptatibus minus vel fuga, animi autem dolor, quibusdam consequatur excepturi. Neque, aut voluptatibus.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomepageMainSectionCards"
}
</script>

<style>
.homepage_section_cards{
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

.main_section_card_grid{
    display: grid;
    grid-template-columns: repeat(auto-fill,minmax(25rem, 1fr));
    grid-template-rows: 1fr;
    gap: 1rem;
}

.main_section_card{
    border: solid 0.5px;
    color: #bccadb;
}
.main_section_card img{
    width: 100%;
    height: 15rem;
    object-fit: cover;
}
.card_content{
    padding: 1.25rem;
    text-align: left;
    justify-content: space-between;
}
.card_content h4{
    color: var(--secondary-color);
    font-size: 1.3rem;
    font-weight: 400;
    line-height: 1.2;
}
.card_content p{
    font-weight: lighter;
    line-height: 1.5;
    margin-top: 1rem;
}
</style>