<template>
  <div>
    <div class="profile">
      <h1>User Profile</h1>
      <h1>{{ companyName }}</h1>
      <p>Material: {{ material }}</p>
      <p>Coordinates: {{ coordinates }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: 'UserProfile',
  props: {
    companyName: String,
    material: String,
    coordinates: String,
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
