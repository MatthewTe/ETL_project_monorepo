<template>
<div class="data_dashboard_card_section">
    <div class="card_grid">
        <h2>Data Dashboards</h2>
        <div class="main_section_card_grid">
            <div class="main_section_card">
                <div class="card_image"><img src="@/assets/core/test.jpg" alt=""></div>
                <div class="card_content">
                    <h4>Stockholm International Peace Research Institute Arms Dashboards</h4>
                    <p>Ceteris paribus publishes various writings ranging from formal articles and whitepapers about our data collection and dashboards to fully opinionated articles by authors discussing contemporary issues mainly in the fields of international economics and foregin policy (or geopolitics depending on where you’re from).</p>
                </div>
                
            </div>

            <div class="main_section_card">
                <div class="card_image"><img src="@/assets/core/Social_Media_Thumbnail.png" alt=""></div>
                <div class="card_content">
                    <h4>Social Media Dashboards</h4>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium facilis earum velit nobis deserunt. Reprehenderit beatae molestiae deserunt id, quia error itaque, esse quaerat rerum dolores minus ad odit necessitatibus.</p>
                </div>
            </div>

            <div class="main_section_card">
                <div class="card_image">
                    <img src="@/assets/core/Zotero_Dashboard.png" alt=""></div>
                <div class="card_content">
                    <h4>Zotero and Research Management Dashboards</h4>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Recusandae odit quod eos praesentium doloribus quaerat aliquam blanditiis voluptatibus minus vel fuga, animi autem dolor, quibusdam consequatur excepturi. Neque, aut voluptatibus.</p>
                </div>
            </div>
        </div>
    </div>    
</div>
</template>

<script>
export default {
    name: "HomepageDataDashboardSectionCards"

}
</script>

<style scoped>
.card_grid{
    padding-top: 2rem;
    padding-left: 4rem;
    padding-right: 4rem;

}
.card_grid h2{
    color: var(--secondary-color);
    text-align: left;
    padding-bottom: 0.5rem;

    
}
</style>