<template>
  <div>
    <div class="profile">
      <h1 class="profile-title">Contractor Profile</h1>
      <h1 class="contractor-name">Contractor Name: {{contractor_name}}</h1>
      <p class="truck-info">Truck: {{ truck }}</p>
      <p class="coordinates-info">Coordinates: {{ coordinates }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ContractorProfile",
  props: {
    contractor_name: String,
    truck: String,
    coordinates: String,
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */

.profile {
  background-color: var(--background-color);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.profile-title {
  color: var(--primary-color);
  margin-bottom: 20px;
  font-size: 24px;
}

.contractor-name,
.truck-info,
.coordinates-info {
  color: var(--primary-color);
  margin-bottom: 10px;
}

</style>
