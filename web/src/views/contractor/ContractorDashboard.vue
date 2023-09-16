<!-- ContractorSchedule.vue -->
<template>
  <div>
    <h1>Contractor Schedule</h1>
    <table>
      <thead>
      <tr>
        <th>Name:</th>
        <th>Status:</th>
        <th>Start Coordinates:</th>
        <th>End Coordinates:</th>
        <th>Cargo Type:</th>
        <th>Weight:</th>
        <th>Start Date:</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="shipment in shipments" :key="shipment._id" @click="viewShipment(shipment)">
        <td>{{ shipment.name }}</td>
        <td>{{ shipment.status }}</td>
        <td>{{ shipment.startCoordinates }}</td>
        <td>{{ shipment.endCoordinates }}</td>
        <td>{{ shipment.cargoType }}</td>
        <td>{{ shipment.weight }}</td>
        <td>{{ shipment.startDate }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'ContractorSchedule',
  data() {
    return {
      shipments: [], // Store the list of shipments
    };
  },
  async mounted() {
    // Fetch shipments for the contractor from your API
    this.shipments = await this.fetchShipments();
  },
  methods: {
    async fetchShipments() {
      try {
        // Make an API request to fetch shipments for the contractor
        const response = await fetch('/api/contractor-shipments'); // Replace with your API endpoint
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
    viewShipment(shipment) {
      // Use Vue Router to navigate to the NavigationPage with the selected shipment
      const router = useRouter();
      router.push({ name: 'ContractorNavigation', params: { shipment: shipment } });
    },
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
