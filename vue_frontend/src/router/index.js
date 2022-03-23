import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/core/HomeView.vue'
import ArticleView from '../views/articles/ArticlesView.vue'
import DataDashboardView from '../views/data_dashboards/DataDashboardsView.vue'
import NorthKoreaView from '../views/north_korea/NorthKoreaIndexView.vue'
import DeveloperDocumentationView from '../views/documentation/DeveloperDocumentationView.vue'
import AboutView from '../views/core/AboutView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleView
  },
  {
    path: '/dashboards',
    name: 'dashboards',
    component: DataDashboardView
  },
  {
    path: '/north_korea',
    name: 'north_korea',
    component: NorthKoreaView
  },
  {
    path: '/developer_documentation',
    name: 'developer_documentation',
    component: DeveloperDocumentationView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
