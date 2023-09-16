<template>
  <div>
    <div class="profile">
      <h1>Contractor Profile</h1>
      <h1>Contractor Name: {{contractor_name}}</h1>
      <p>Truck: {{ truck }}</p>
      <p>Coordinates: {{ coordinates }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: 'UserProfile',
  props: {
    contractor_name: String,
    truck: String,
    coordinates: String,
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
