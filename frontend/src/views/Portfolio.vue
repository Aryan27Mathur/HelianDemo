<template>
  <div>
    <v-container class="h-screen mt-12 px-12 py-4 align-center">
      <v-row>
        <v-col cols="12">
          <h1 class="mx-auto text-center">Portfolio Analysis</h1>
          <p class="mx-auto mt-8 w-50 text-center">
            Below is a tool that allows you to visualize and understand the
            impact of your trading portfolio in terms of ESG. Helian currently
            supports robinhood brokerage accounts only. Go to
            <br />
            <b>https://robinhood.com/account/reports-statements/brokerage</b>
            <br /><br />
            and select your most recent monthly statement from your brokerage
            account
            <br /><br />
          </p>
          <v-img
            class="elevation-4"
            src="/src/assets/robinhood_screeshot.png"
          ></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-spacer></v-spacer>
        </v-col>
        <v-col class="px-4" cols="2" justify="center">
          <v-btn block color="teal darken-1">Submit</v-btn>
        </v-col>
        <v-col>
          <v-spacer></v-spacer>
        </v-col>
      </v-row>
    </v-container>
    <MyFooter />
  </div>
</template>

<script setup lang="ts"></script>
