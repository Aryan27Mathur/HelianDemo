<template>
  <v-app>
    <v-main>
      <Navbar />
      <transition name="fade">
        <router-view v-slot="{ Component }">
          <component :is="Component" />
        </router-view>
      </transition>
    </v-main>
  </v-app>
</template>

<script setup lang="ts"></script>

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
