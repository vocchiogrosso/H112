<template>
  <div class="navigation-container">
    <h1 class="navigation-title">Contractor Navigation</h1>
    <div class="destination-input">
    </div>
    <div id="map-container" class="map"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import mapboxgl from 'mapbox-gl';
import { useRouter } from "vue-router";

const user = JSON.parse(sessionStorage.getItem('user'));
const _id = new URLSearchParams(window.location.search).get('_id');

export default defineComponent({
  name: 'ContractorNavigation',

  data() {
    return {
      map: null,
      destinationInput: '',
    };
  },

  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoicS1oZSIsImEiOiJjbG1tenU5M3Ywcm10MmtsODRkNXl2czg1In0.8LIrsjDVclchBgYXxDt-hg';

    this.map = new mapboxgl.Map({
      container: 'map-container',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-74.5, 40],
      zoom: 9,
    });
  },

  async beforeMount() {
    const user = sessionStorage.getItem('user');
    const router = this.$router;
    if (user === null || user === undefined) {
      await router.push({ name: 'Auth' });
    }
    if (user.includes('normal')) {
      await router.push({ name: 'UserDashboard' });
    }
    const shipment = await this.fetchShipments();

    // Calculate the route using a routing API (e.g., Mapbox Directions API)
    const route = await this.calculateRouteToDestination(shipment);

    // Display the route on the map
    this.displayRoute(route);
  },

  methods: {
    async fetchShipments() {
      try {
        const user = JSON.parse(sessionStorage.getItem('user'));

        // Make an API request to fetch shipments for the contractor
        const response = await fetch('http://localhost:4000/api/shipments/get/' + _id, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.token}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch shipments');
        }
        const data = await response.json();
        console.log(data);
        return data;
      } catch (error) {
        console.error('Error fetching shipments:', error);
        return [];
      }
    },

    async calculateRouteToDestination(shipment) {
      console.log(shipment);
      // Use a routing API to calculate the route to the destination
      // Example: Make an API request and parse the response
      // Replace this with the actual routing API you are using (Mapbox Directions API)
      // Here's the code from the previous response:
      const accessToken = 'pk.eyJ1IjoicS1oZSIsImEiOiJjbG1tenU5M3Ywcm10MmtsODRkNXl2czg1In0.8LIrsjDVclchBgYXxDt-hg';
      const startCoordinates = [shipment.startCoordinates.ltd, shipment.startCoordinates.lng];
      const destinationCoordinates = [shipment.endCoordinates.ltd, shipment.endCoordinates.lng];
      console.log(startCoordinates, destinationCoordinates);

      // Construct the API URL for the Mapbox Directions API
      const apiUrl = `https://api.mapbox.com/directions/v5/mapbox/driving-traffic/${startCoordinates[0]},${startCoordinates[1]};${destinationCoordinates[0]},${destinationCoordinates[1]}?annotations=distance%2Cduration&geometries=geojson&language=en&overview=full&steps=true`; // or steps=false, depending on your preference

      // Add query parameters
      const params = new URLSearchParams({
        access_token: accessToken,
      });

      // Fetch the route from the API
      try {
        const response = await fetch(`${apiUrl}&${params.toString()}`, {
          headers: {
            'Authorization': `Bearer ${accessToken}`,
          },
        });
        if (!response.ok) {
          throw new Error('Failed to fetch route data');
        }
        const data = await response.json();
        console.log(data);
        return data.routes[0]; // Assuming you want the first route
      } catch (error) {
        console.error('Error calculating route:', error);
        return null;
      }
    },

    displayRoute(route) {
      // Use Mapbox GL JS to display the route on the map
      this.map.addSource('route', {
        type: 'geojson',
        data: {
          type: 'Feature',
          properties: {},
          geometry: route.geometry,
        },
      });

      this.map.addLayer({
        id: 'route',
        type: 'line',
        source: 'route',
        layout: {
          'line-join': 'round',
          'line-cap': 'round',
        },
        paint: {
          'line-color': '#0074D9',
          'line-width': 4,
        },
      });

      // Fit the map to the bounds of the route
      const bounds = new mapboxgl.LngLatBounds(route.geometry.coordinates);
      this.map.fitBounds(bounds, { padding: 50 });
    },
  },
});
</script>

<style scoped>
/* Component-specific styles */
.navigation-container {
  background-color: var(--background-color);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 80%;
  margin: 0 auto;
  text-align: center;
}

.navigation-title {
  color: var(--primary-color);
  font-size: 24px;
  margin-bottom: 20px;
}

.destination-input {
  margin-bottom: 20px;
}

.input-label {
  font-weight: bold;
  color: var(--text-color);
}

.input-field {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 4px;
  width: 100%;
}

.map {
  width: 100%;
  height: 400px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
