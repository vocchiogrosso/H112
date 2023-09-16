<!-- RequestForm.vue -->
<template>
  <form @submit.prevent="submitForm">
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" v-model="formData.title" required />
    </div>
    <div>
      <label for="startCoordinates">Start Coordinates:</label>
      <input type="text" id="startCoordinates" v-model="formData.startCoordinates" required />
    </div>
    <div>
      <label for="endCoordinates">End Coordinates:</label>
      <input type="text" id="endCoordinates" v-model="formData.endCoordinates" required />
    </div>
    <div>
      <label for="cargoType">Cargo Type:</label>
      <input type="text" id="cargoType" v-model="formData.cargoType" required />
    </div>
    <div>
      <label for="weight">Weight:</label>
      <input type="number" id="weight" v-model="formData.weight" required />
    </div>
    <div>
      <label for="startDate">Start Date:</label>
      <input type="date" id="startDate" v-model="formData.startDate" required />
    </div>
    <div>
      <button type="submit">Submit Request</button>
    </div>
  </form>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'RequestForm',
  data() {
    return {
      formData: {
        title: '',
        startCoordinates: '',
        endCoordinates: '',
        cargoType: '',
        weight: '',
        startDate: '',
      },
    };
  },
  methods: {
    async submitForm() {
      try {
        // Send a POST request with the form data to your API endpoint
        const response = await fetch('/api/requests', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        });

        if (response.ok) {
          // Request was successful, you can perform further actions if needed
          console.log('Request submitted successfully');
        } else {
          // Handle errors here
          console.error('Request submission failed');
        }
      } catch (error) {
        console.error('Error submitting request:', error);
      }
    },
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
