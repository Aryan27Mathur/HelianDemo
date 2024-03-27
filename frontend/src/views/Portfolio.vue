<template>
  <div>
    <v-container class="my-6 px-12 py-8 align-center elevation-2">
      <v-row>
        <v-col cols="12">
          <h1 class="mx-auto text-center">Portfolio Analysis</h1>
          <p class="mx-auto mt-8 w-75 text-center">
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
      <v-row class="mt-12">
        <v-col> </v-col>
        <v-col class="px-4" cols="6" justify="center">
          <v-file-input
            v-model="selectedFile"
            color="teal-darken-1"
            label="Portfolio PDF"
          ></v-file-input>
          <p>{{ myIp }}</p>
        </v-col>
        <v-col> </v-col>
      </v-row>
      <v-row>
        <v-col> </v-col>
        <v-col class="px-4" cols="2" justify="center">
          <v-btn block color="teal-darken-1" @click="submitForm">Submit</v-btn>
        </v-col>
        <v-col> </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-data-table v-if="data.length > 0" :items="data"></v-data-table>
        </v-col>
      </v-row>
    </v-container>
    <MyFooter />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Define a reactive variable to store the selected file
const selectedFile = ref([]);
const myIp = ref("");
const data = ref([]);
// Define a method to handle form submission
const submitForm = async () => {
  const file = selectedFile.value[0];
  if (file) {
    // Create FormData object to send file
    const formData = new FormData();
    formData.append("file", file);

    try {
      // Make a POST request using fetch
      const response = await fetch("http://localhost:8000/post_portfolio/", {
        method: "POST",
        body: formData,
        // headers: {
        //   "Content-Type": "multipart/form-data",
        // },
      });
      // const response = await fetch(
      //   "http://localhost:8000/get_all_company_symbols/"
      // );

      // Parse the JSON response
      const responseData = await response.json();
      data.value = responseData["portfolio"];
      console.log("Response from backend:", responseData);
    } catch (error) {
      console.error("Error:", error);
    }
  } else {
    console.log("No file selected.");
  }
};
</script>
