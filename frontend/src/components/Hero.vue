<template>
  <v-container>
    <v-row>
      <v-col class="my-auto ml-8">
        <div class="text-h3 py-4">Invest Sustainably with Helian</div>

        <!-- Subtext area -->
        <div class="text-subtitle-1 py-4">
          Learn about the true environmental and social impact behind the
          companies you invest in, make better informed decisions, and get
          investment recommendations based on your personal values. To learn
          more about our services, platform, or to keep up to date with us, join
          our newsletter.
        </div>
        <v-text-field
          v-model="email"
          @keydown.enter="handleEnterKey"
          density="compact"
          placeholder="Email address"
          color=""
          prepend-inner-icon="mdi-email-outline"
          variant="solo"
        ></v-text-field>
        <p v-if="signupMessage">{{ signupMessage }}</p>
        <!-- Button -->
      </v-col>
      <!-- Right column -->
      <v-col cols="8" md="4" class="ma-10">
        <!-- Image -->
        <img src="/src/assets/forest.svg" alt="Image" class="img-fluid" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
import axios from "axios";

const email = ref("");
const signupMessage = ref("");

async function handleEnterKey() {
  // Client-side email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email.value)) {
    signupMessage.value = "Please enter a valid email.";
    return;
  }

  // If email is valid, set the signupMessage and send request to backend
  signupMessage.value =
    "Thanks for signing up! Check back for future updates to Helian.";
  email.value = "";
  try {
    await axios.post<{ message: string }>(
      "https://helian-backend.onrender.com/newuser/",
      {
        name: "",
        email: email.value,
      }
    );
    // Optionally, you can clear the email input after successful signup
  } catch (error) {
    console.error("Error:", error);
    signupMessage.value = "An error occurred while signing up.";
  }
}
</script>
