<template>
    <v-footer class="bg-teal-darken-4" outlined>
      <v-row justify="center" no-gutters>
        <v-btn color="white" variant="text" class="mx-2 px-auto" rounded="xl">The Team</v-btn>
        <v-btn color="white" variant="text" class="mx-2 px-auto" rounded="xl">Services</v-btn>
        <v-btn color="white" variant="text" class="mx-2 px-auto" rounded="xl">Contact Us</v-btn>
        <v-col class="text-center mt-4" cols="12">
          {{ new Date().getFullYear() }} — <strong>Helian</strong>
        </v-col>
      </v-row>
    </v-footer>
  </template>
  
  <script setup lang="ts">

  </script>