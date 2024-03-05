<template>
  <div>
    <v-card elevation="12" class="ma-8">
      <v-container class="h-100">
        <v-row class="mt-12">
          <v-spacer></v-spacer>
          <v-col>
            <h1 class="text-center">Try our Services</h1>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
        <v-row class="mb-12">
          <v-col>
            <v-card class="mx-auto my-8 pa-4" elevation="16" max-width="600">
              <v-card-item>
                <v-card-title class="text-center">
                  Recommendation System
                </v-card-title>
                <v-img max-height="125" src="/src/assets/quality.png"></v-img>
              </v-card-item>

              <v-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </v-card-text>
              <v-card-actions class="justify-center">
                <router-link to="/rec">
                  <v-btn color="teal darken-1">Try Now</v-btn>
                </router-link>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="mx-auto my-8 pa-4" elevation="16" max-width="600">
              <v-card-item>
                <v-card-title class="text-center">
                  Portfolio Analysis
                </v-card-title>
                <v-img
                  max-height="125"
                  src="/src/assets/investment.png"
                ></v-img>
              </v-card-item>

              <v-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </v-card-text>
              <v-card-actions class="justify-center">
                <router-link to="/portfolio">
                  <v-btn color="teal darken-1">Try Now</v-btn>
                </router-link>
              </v-card-actions>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="mx-auto my-8 pa-4" elevation="16" max-width="600">
              <v-card-item>
                <v-card-title class="text-center">
                  Trading Platform
                </v-card-title>
                <v-img max-height="125" src="/src/assets/dashboard.png"></v-img>
              </v-card-item>

              <v-card-text>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </v-card-text>
              <v-card-actions class="justify-center">
                <v-btn disabled color="teal darken-1">Coming Soon</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <MyFooter />
  </div>
</template>

<script setup lang="ts">
//
</script>
