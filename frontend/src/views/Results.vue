<template>
  <div>
    <v-container fluid class="my-8">
      <v-row justify="center">
        <v-col cols="12" md="6">
          <v-card variant="elevated">
            <!-- Card content goes here -->

            <v-container class="px-12 py-4">
              <v-row justify="center">
                <v-col cols="12">
                  <h2 class="display-1 text-center">
                    Results - Your Top Helian Companies
                  </h2>
                  <p class="body-1 px-12">
                    Below are the top recommendations for companies you should
                    invest in based on your personal values. To learn more about
                    our process, sign up to our platform and newsletter.
                  </p>
                </v-col>
              </v-row>
              <v-row v-if="isLoading" justify="center">
                <v-col cols="12" class="text-center">
                  <v-progress-circular
                    indeterminate
                    color="green"
                  ></v-progress-circular>
                </v-col>
              </v-row>

              <!-- Company list -->
              <v-row v-if="!isLoading" justify="center">
                <v-col cols="12">
                  <v-list lines="two" class="text-center">
                    <v-list-item
                      v-for="company in companies"
                      :key="company.ticker"
                    >
                      <v-list-item-title>{{
                        company.ticker
                      }}</v-list-item-title>
                      <v-list-item-subtitle>{{
                        company.name
                      }}</v-list-item-subtitle>
                    </v-list-item>
                  </v-list>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <MyFooter v-if="!isLoading"></MyFooter>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const isLoading = ref(true);
const companies = ref([
  {
    ticker: "AAPL",
    name: "Apple Inc.",
    industry: "Technology",
    esgRating: "AAA",
    esg_report:
      "https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2023.pdf",
  },
  {
    ticker: "MSFT",
    name: "Microsoft Corporation",
    industry: "Technology",
    esgRating: "AAA",
    esg_report:
      "https://www.microsoft.com/en-us/corporate-responsibility/impact-summary",
  },
  {
    ticker: "GOOGL",
    name: "Alphabet Inc.",
    industry: "Technology",
    esgRating: "AAA",
    esg_report:
      "https://sustainability.google/reports/google-2023-environmental-report/",
  },
  {
    ticker: "FB",
    name: "Meta Platforms Inc.",
    industry: "Technology",
    esgRating: "AAA",
    esg_report: "https://sustainability.fb.com/2023-sustainability-report/",
  },
  {
    ticker: "TSLA",
    name: "Tesla Inc.",
    industry: "Electric Vehicles",
    esgRating: "AAA",
    esg_report: "https://www.tesla.com/impact",
  },
  {
    ticker: "BRK.A",
    name: "Berkshire Hathaway Inc.",
    industry: "Finance",
    esgRating: "AAA",
  },
  {
    ticker: "NVDA",
    name: "NVIDIA Corporation",
    industry: "Technology",
    esgRating: "AAA",
    esg_report:
      "https://images.nvidia.com/aem-dam/Solutions/documents/FY2023-NVIDIA-Corporate-Responsibility-Report-1.pdf",
  },
  {
    ticker: "JPM",
    name: "JPMorgan Chase & Co.",
    industry: "Finance",
    esgRating: "AAA",
    esg_report: "https://www.jpmorganchase.com/impact/sustainability",
  },
  {
    ticker: "V",
    name: "Visa Inc.",
    industry: "Finance",
    esgRating: "AAA",
    esg_report:
      "https://vgrouplimited.com/sustainability-within-the-maritime-industry/reporting/",
  },
  {
    ticker: "FSLR",
    name: "First Solar, Inc.",
    industry: "Renewable Energy",
    esgRating: "AAA",
  },
  {
    ticker: "NEE",
    name: "NextEra Energy, Inc.",
    industry: "Renewable Energy",
    esgRating: "AAA",
    esg_report:
      "https://www.nexteraenergy.com/content/dam/nee/us/en/pdf/2023_NEE_Sustainability_Report_Final.pdf",
  },
  {
    ticker: "ENPH",
    name: "Enphase Energy, Inc.",
    industry: "Renewable Energy",
    esgRating: "AAA",
    esg_report:
      "https://investor.enphase.com/news-releases/news-release-details/enphase-energy-releases-2022-environmental-social-and-governance",
  },
  // Add more companies with their ticker symbols, names, industries, and hypothetical ESG ratings as needed
]);

// Randomize the companies array
companies.value.sort(() => Math.random() - 0.5);

// Simulate loading delay with a timeout
setTimeout(() => {
  isLoading.value = false;
}, 2000);
</script>
