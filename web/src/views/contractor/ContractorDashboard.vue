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
        <td>{{ shipment.title }}</td>
        <td>{{ shipment.status }}</td>
        <td>{{ shipment.startCoordinates.ltd }}, {{shipment.startCoordinates.lng}}</td>
        <td>{{ shipment.endCoordinates.ltd }}, {{shipment.endCoordinates.lng}}</td>
        <td>{{ shipment.typeOfShipment }}</td>
        <td>{{ shipment.weight }}</td>
        <td>{{ new Date(shipment.pickupTime) }}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ContractorDashboard',
  data() {
    return {
      shipments: [], // Store the list of shipments
    };
  },
  async mounted() {
    // Fetch shipments for the contractor from your API
    this.shipments = await this.fetchShipments();
  },
  async beforeMount() {
    const user = sessionStorage.getItem('user')
    const router = this.$router;
    if (user === null || user === undefined){
      await router.push({ name: 'Auth' });
    }
    if (user.includes( 'normal')){
      await router.push({ name: 'UserDashboard' });
    }

  },
  methods: {
    async fetchShipments() {
      try {
        const user = JSON.parse(sessionStorage.getItem('user'))

        // Make an API request to fetch shipments for the contractor
        const response = await fetch('http://localhost:4000/api/shipments/getAll/' + user._id, {

          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.token}`
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch shipments');
        }
        const data = await response.json();
        console.log(data)
        return data;
      } catch (error) {
        console.error('Error fetching shipments:', error);
        return [];
      }
    },
    viewShipment(shipment) {
      // Use Vue Router to navigate to the NavigationPage with the selected shipment
      const router = this.$router;
      router.push({ name: 'ContractorNavigation', params: { _id: (shipment._id) } });
    },
  },
});
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
