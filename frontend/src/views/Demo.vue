<template>
    <v-card variant="elevated" class="ma-8">
        <v-container class="px-12 py-4">
        <v-row justify="center">
            <v-col cols="12">
            <h2 class="display-1 text-center">Demo - Helian Reccomendation System</h2>
            <p class="body-1 px-12">This form is designed to understand your personal preferences regarding the UN's 17 SDG targets. The SDGs cover a wide range of global challenges, from poverty eradication and environmental sustainability to education and gender equality. After you submit, we will recommend the top US companies to invest in based on your personal preferences.</p>
            </v-col>
        </v-row>
        </v-container>
      <!-- Loop through SDG targets and render sliders -->
        <v-row v-for="(sdg, index) in sdgs" :key="index">
          <v-col cols="12">
            <v-container class="px-8 my-1 elevation-1 bg-white">
            <h3>SDG {{ sdg.number }}: {{ sdg.title }}</h3>
            <label class="slider-label">{{ sdg.description }}</label>
            <v-slider class="py-4" v-model="sdg.value" :min="1" :max="10">
                <template v-slot:prepend>Low priority for me</template>
                <template v-slot:append>High priority for me</template>
            </v-slider>
            <p class="slider-value">Value: {{ Math.round(sdg.value) }}</p>
        </v-container>
          </v-col>
        </v-row>
      <v-row>
            <v-col cols="12" class="text-center my-4">
                <v-btn color="teal darken-1">Submit</v-btn>
            </v-col>
        </v-row>
    </v-card>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  interface SDG {
    number: string;
    title: string;
    description: string;
    value: number;
  }
  
  const sdgs = ref<SDG[]>([
  { number: '1', title: 'No Poverty', description: 'End poverty in all its forms everywhere.', value: 1 },
  { number: '2', title: 'Zero Hunger', description: 'End hunger, achieve food security and improved nutrition and promote sustainable agriculture.', value: 1 },
  { number: '3', title: 'Good Health and Well-being', description: 'Ensure healthy lives and promote well-being for all at all ages.', value: 1 },
  { number: '4', title: 'Quality Education', description: 'Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.', value: 1 },
  { number: '5', title: 'Gender Equality', description: 'Achieve gender equality and empower all women and girls.', value: 1 },
  { number: '6', title: 'Clean Water and Sanitation', description: 'Ensure availability and sustainable management of water and sanitation for all.', value: 1 },
  { number: '7', title: 'Affordable and Clean Energy', description: 'Ensure access to affordable, reliable, sustainable and modern energy for all.', value: 1 },
  { number: '8', title: 'Decent Work and Economic Growth', description: 'Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all.', value: 1 },
  { number: '9', title: 'Industry, Innovation, and Infrastructure', description: 'Build resilient infrastructure, promote inclusive and sustainable industrialization, and foster innovation.', value: 1 },
  { number: '10', title: 'Reduced Inequalities', description: 'Reduce inequality within and among countries.', value: 1 },
  { number: '11', title: 'Sustainable Cities and Communities', description: 'Make cities and human settlements inclusive, safe, resilient and sustainable.', value: 1 },
  { number: '12', title: 'Responsible Consumption and Production', description: 'Ensure sustainable consumption and production patterns.', value: 1 },
  { number: '13', title: 'Climate Action', description: 'Take urgent action to combat climate change and its impacts.', value: 1 },
  { number: '14', title: 'Life Below Water', description: 'Conserve and sustainably use the oceans, seas and marine resources for sustainable development.', value: 1 },
  { number: '15', title: 'Life on Land', description: 'Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss.', value: 1 },
  { number: '16', title: 'Peace, Justice, and Strong Institutions', description: 'Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels.', value: 1 },
  { number: '17', title: 'Partnerships for the Goals', description: 'Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development.', value: 1 }
]);
  
  </script>
  
  <style scoped>

  </style>
  