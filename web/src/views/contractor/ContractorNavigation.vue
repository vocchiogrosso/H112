<template>
  <div>
    <h1>Contractor Navigation</h1>
    <div>
      <label for="destination">Enter Destination:</label>
      <input
          id="destination"
          type="text"
          v-model="destinationInput"
      />
      <button @click="calculateRoute">Calculate Route</button>
    </div>
    <div id="map-container" style="width: 100%; height: 400px;"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import mapboxgl from 'mapbox-gl';

export default defineComponent({
  name: 'ContractorNavigation',

  data() {
    return {
      map: null,
      destinationInput: '',
    };
  },

  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoiejRsM3M1aTAiLCJhIjoiY2xtbTd1NDB6MGttNDJxcG5mZHpqbXJsMiJ9.m9i3527cJA3QTJgPLPIWHg';

    this.map = new mapboxgl.Map({
      container: 'map-container',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-74.5, 40],
      zoom: 9,
    });
  },

  methods: {
    async calculateRoute() {
      // Fetch coordinates for the user's destination input from a geocoding API
      const destinationCoordinates = await this.fetchDestinationCoordinates(this.destinationInput);

      // Calculate the route using a routing API (e.g., Mapbox Directions API)
      const route = await this.calculateRouteToDestination(destinationCoordinates);

      // Display the route on the map
      this.displayRoute(route);
    },

    async fetchDestinationCoordinates(destinationInput) {
      // Use a geocoding API to fetch coordinates for the destination input
      // Example: Make an API request and parse the response
      // Replace this with the actual geocoding API you are using
      // const response = await fetch(`YOUR_GEOCODING_API_URL?query=${destinationInput}`);
      // const data = await response.json();
      // const coordinates = data.features[0].geometry.coordinates;
      // return coordinates;
      // For now, let's use a mock response for demonstration
      return [-74.6, 40.1];
    },

    async calculateRouteToDestination(destinationCoordinates) {
      // Use a routing API to calculate the route to the destination
      // Example: Make an API request and parse the response
      // Replace this with the actual routing API you are using (Mapbox Directions API)
      // Here's the code from the previous response:
      const accessToken = 'pk.eyJ1IjoiejRsM3M1aTAiLCJhIjoiY2xtbTd1NDB6MGttNDJxcG5mZHpqbXJsMiJ9.m9i3527cJA3QTJgPLPIWHg';
      const startCoordinates = [-74.5, 40]; // Replace with the actual starting coordinates
      const max_weight = 2.5;
      const max_heigth = 1.6;
      const max_width = 1.9;

      // Construct the API URL for the Mapbox Directions API
      const apiUrl = `https://api.mapbox.com/directions/v5/mapbox/driving-traffic/${startCoordinates[0]},${startCoordinates[1]};${destinationCoordinates[0]},${destinationCoordinates[1]}&annotations=distance%2Cduration&geometries=geojson&language=en&overview=full&steps=true&max_height=${max_heigth}&max_width=${max_width}&max_weight=${max_weight}`;


      // Add query parameters
      const params = new URLSearchParams({
        access_token: accessToken,
      });

      // Fetch the route from the API
      try {
        const response = await fetch(`${apiUrl}&${params.toString()}`);
        if (!response.ok) {
          throw new Error('Failed to fetch route data');
        }
        const data = await response.json();
        console.log(data)
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
