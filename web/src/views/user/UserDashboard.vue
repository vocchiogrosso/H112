<template>
  <div>
    <h1>User Dashboard</h1>
    <router-link to="/user/request-form">
      <button>Go to Request Form</button>
    </router-link>

    <div v-if="shipments.length">
      <h2>Shipments:</h2>
      <ul>
        <li v-for="shipment in shipments" :key="shipment._id">
          {{ shipment.name }} - {{ shipment.status }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'UserDashboard',
  data() {
    return {
      shipments: [],
    };
  },
  async mounted() {
    // Fetch shipments from an API here and update the shipments array
    this.shipments = await this.fetchShipments();
  },
  methods: {
    async fetchShipments() {
      try {
        // Make an API request to fetch shipments
        const response = await fetch('/api/shipments'); // Replace with your API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch shipments');
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error('Error fetching shipments:', error);
        return [];
      }
    },
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
