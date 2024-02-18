/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

//Views
import Demo from './views/Demo.vue'
import Home from './views/Home.vue'
// Composables
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {path: "/demo", component: Demo},
    {path: "", component: Home}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App).use(router)

registerPlugins(app)

app.mount('#app')
