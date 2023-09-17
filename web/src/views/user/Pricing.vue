<template>
  <div id="pricing" class="pricing-container">
    <h1 class="pricing-title">Truck Pricing Calculator</h1>

    <div class="input-group">
      <label for="distance" class="input-label">Distance (in miles): </label>
      <input type="number" id="distance" v-model="distance" class="input-field" />
    </div>

    <div class="input-group">
      <label for="materials" class="input-label">Materials Type: </label>
      <select id="materials" v-model="selectedMaterial" class="input-select">
        <option value="ESCORIA DE SUELO">ESCORIA DE SUELO</option>
        <option value="LODOS DE REDI">LODOS DE REDI</option>
        <option value="FINOS DE OXIDOS DE FE">FINOS DE OXIDOS DE FE</option>
        <!-- Add more material options as needed -->
      </select>
    </div>

    <div class="input-group">
      <label for="weight" class="input-label">Weight (in tons): </label>
      <input type="number" id="weight" v-model="weight" class="input-field" />
    </div>

    <div class="result">
      <h2 class="result-title">Estimated Price: ${{ calculatePrice }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      distance: 0,
      selectedMaterial: 'ESCORIA DE SUELO',
      weight: 0,
    };
  },

  async beforeMount(){
    const user = sessionStorage.getItem('user')
    const router = this.$router;
    if (user === null || user === undefined){
      await router.push({ name: 'Auth' });
    }
    if (user.includes('contractor')){
      await router.push({ name: 'ContractorDashboard' });
    }
  },
  computed: {
    calculatePrice() {
      // Adjust this pricing formula based on your needs
      let basePrice = 500; // Base price for transportation
      let distancePrice = this.distance * 9; // $0.10 per mile
      let materialPrice = 3;

      // Adjust material prices based on your needs
      if (this.selectedMaterial === 'ESCORIA DE SUELO') {
        materialPrice = this.weight * 2; // $0.20 per pound for steel
      } else if (this.selectedMaterial === 'LODOS DE REDI') {
        materialPrice = this.weight * 1.5; // $0.15 per pound for wood
      } else if (this.selectedMaterial === 'FINOS DE OXIDOS DE FE') {
        materialPrice = this.weight * 2.5; // $0.25 per pound for concrete
      }

      // Calculate the total price
      let totalPrice = basePrice + distancePrice + materialPrice;

      return totalPrice.toFixed(2); // Format to two decimal places
    },
  },
};
</script>

<style>
.pricing-container {
  background-color: var(--background-color);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px; /* Adjust the width as needed */
  margin: 0 auto; /* Center the calculator horizontally */
  text-align: center; /* Center-align the calculator items */
}

.pricing-title {
  font-size: 24px;
  color: var(--primary-color);
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 16px;
  text-align: left; /* Left-align the input field labels */
}

.input-label {
  display: block;
  margin-bottom: 8px;
  color: var(--primary-color);
}

.input-field,
.input-select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: var(--background-color);
  color: var(--primary-color);
}

.input-field:focus,
.input-select:focus {
  outline: none;
  border-color: var(--accent-color);
}

.result-title {
  font-size: 20px;
  margin-top: 20px;
  color: var(--accent-color);
}

</style>
