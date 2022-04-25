<template>
  <div class="home">
    <HomepageMasthead/>
    <HomepageMainSectionCards/>
    <HomepageDataDashboardSectionCards/>
    <HomepageArticleCards/>
  </div>
</template>

<script>
import HomepageMasthead from '@/components/core/Homepage_Masthead.vue'
import HomepageMainSectionCards from '@/components/core/Homepage_Section_Cards.vue'
import HomepageDataDashboardSectionCards from '@/components/core/Homepage_Dashboard_Section_Cards.vue'
import HomepageArticleCards from '@/components/core/Homepage_Article_Cards_Section.vue'

export default {
  name: 'HomeView',
  components: {
    HomepageMasthead,
    HomepageMainSectionCards,
    HomepageDataDashboardSectionCards,
    HomepageArticleCards
  }
}
</script>
