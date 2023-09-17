<template>
  <div class="form-container">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="formData.title" required />
      </div>
      <div class="form-group">
        <label for="startCoordinates">Start Coordinates:</label>
        <input type="text" id="startCoordinates" v-model="formData.startCoordinates" required />
      </div>
      <div class="form-group">
        <label for="endCoordinates">End Coordinates:</label>
        <input type="text" id="endCoordinates" v-model="formData.endCoordinates" required />
      </div>
      <div class="form-group">
        <label for="typeOfShipment">Cargo Type:</label>
        <select id="typeOfShipment" v-model="formData.typeOfShipment" required>
          <option value="Option1">Option 1</option>
          <option value="Option2">Option 2</option>
          <option value="Option3">Option 3</option>
        </select>
      </div>
      <div class="form-group">
        <label for="weight">Weight:</label>
        <input type="number" id="weight" v-model="formData.weight" required />
      </div>
      <div class="form-group">
        <label for="pickupTime">Start Date:</label>
        <input type="date" id="pickupTime" v-model="formData.pickupTime" required />
      </div>
      <div class="form-group">
        <button type="submit" class="submit-button">Submit Request</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import router from "../../router";

export default defineComponent({
  name: 'RequestForm',
  data() {
    return {
      formData: {
        title: '',
        startCoordinates: '',
        endCoordinates: '',
        typeOfShipment: '',
        weight: '',
        pickupTime: '',
      },
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
  methods: {
    async submitForm() {
      try {
        const user = JSON.parse(sessionStorage.getItem('user'))
        const body = {title: this.formData.title, startCoordinates: {lng: this.formData.startCoordinates.split(',')[0], ltd: this.formData.startCoordinates.split(',')[1]},endCoordinates: {lng: this.formData.endCoordinates.split(',')[0], ltd: this.formData.endCoordinates.split(',')[1]},
          pickupTime: this.formData.pickupTime, typeOfShipment: this.formData.typeOfShipment, weight: this.formData.weight, _id: user._id}
        console.log(this.formData.title)
        // Send a POST request with the form data to your API endpoint
        const response = await fetch('http://localhost:4000/api/shipments/create', {
          method: 'POST',
          body: JSON.stringify(body),
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.token}`
          },
        });

        if (response.ok) {
          // Request was successful, you can perform further actions if needed
          console.log('Request submitted successfully');
          const router = this.$router;
          router.push({ name: 'Pricing'});

        } else {
          // Handle errors here
          console.log(response)
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
.form-container {
  background-color: var(--background-color);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px; /* Adjust the width as needed */
  margin: 0 auto; /* Center the form horizontally */
  text-align: center; /* Center-align the form items */
}

.form-group {
  margin-bottom: 16px;
  text-align: left; /* Left-align the form field labels and inputs within the .form-group */
}

label {
  display: block;
  margin-bottom: 8px;
  color: var(--primary-color);
}

input[type="text"],
input[type="number"],
input[type="date"],
select { /* Apply styles to the select element */
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: var(--background-color); /* Background color */
  color: var(--primary-color); /* Text color */
}

input[type="text"]:focus,
input[type="number"]:focus,
input[type="date"]:focus,
select:focus { /* Apply styles when the select is focused */
  outline: none;
  border-color: var(--accent-color);
}

.submit-button {
  background-color: var(--accent-color);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0077b6; /* Darker shade of accent color on hover */
}
</style>
