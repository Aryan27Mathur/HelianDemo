<template>
  <v-app>
    <v-main>
      <Navbar />
      <router-view v-slot="{ Component }">
        <transition name="fade">
          <component :is="Component" />
        </transition>
      </router-view>
      <MyFooter />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
</script>

<style>
  .fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>