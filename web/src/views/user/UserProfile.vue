<template>
  <div>
    <div class="profile">
      <h1 class="company-name">{{ companyName }}</h1>
      <p class="material">Material: {{ material }}</p>
      <p class="coordinates">Coordinates: {{ coordinates }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

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
.profile {
  background-color: var(--background-color);
  color: var(--primary-color);
  padding: 20px;
}

.company-name {
  font-size: 24px;
  color: var(--accent-color);
}

.material,
.coordinates {
  font-size: 18px;
  margin-top: 10px;
}

</style>
