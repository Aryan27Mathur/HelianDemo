/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from "@/plugins";

// Components
import App from "./App.vue";

//Views
import Demo from "./views/Demo.vue";
import Home from "./views/Home.vue";
import Recs from "./views/Recs.vue";
import Results from "./views/Results.vue";
import Portfolio from "./views/Portfolio.vue";
// Composables
import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  { name: "rec", path: "/rec", component: Recs },
  { name: "home", path: "", component: Home },
  { name: "recresults", path: "/rec/results", component: Results },
  { name: "demo", path: "/demo", component: Demo },
  { name: "portfolio", path: "/portfolio", component: Portfolio },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App).use(router);

registerPlugins(app);

app.mount("#app");
