<template>
    <v-container>
      <v-toolbar color="transparent">
        <router-link to="/">
          <v-btn variant="text" :ripple="false" color="teal darken-2" class="font-weight-bold text-h4">Helian</v-btn>
        </router-link>
        <v-spacer></v-spacer>
        <router-link to='/demo'>
          <v-btn variant="flat" color="teal darken-1" class="font-weight-bold" rounded="xl">Try Now</v-btn>
        </router-link>
        <v-btn color="teal darken-1" class="font-weight-bold">About</v-btn>
        <v-btn color="teal darken-1" class="font-weight-bold">Contact</v-btn>
        <v-btn color="teal darken-1" class="font-weight-bold">Log In</v-btn>
        <v-btn variant="flat" color="teal darken-1" class="font-weight-bold" rounded="xl">Sign Up</v-btn>
      </v-toolbar>
    </v-container>
</template>

<script setup lang="ts">
  //
</script>
