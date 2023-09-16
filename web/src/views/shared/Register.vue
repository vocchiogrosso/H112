<template>
  <div class="register-container">
    <h1 class="register-title">Register Vue</h1>
    <form @submit.prevent="register" class="register-form">
      <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input type="text" id="username" v-model="username" class="form-input" />
      </div>
      <div class="form-group">
        <label for="email" class="form-label">Email:</label>
        <input type="email" id="email" v-model="email" class="form-input" />
      </div>
      <div class="form-group">
        <label for="password" class="form-label">Password:</label>
        <input type="password" id="password" v-model="password" class="form-input" />
      </div>
      <div class="form-group">
        <button type="submit" class="submit-button">Register</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from "vue-router";

export default defineComponent({
  name: 'RegisterVue',

  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      // Construct the registration data
      const registrationData = {
        name: this.username,
        email: this.email,
        password: this.password,
      };

      try {
        const response = await fetch('/api/users/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(registrationData),
        });

        if (!response.ok) {
          // Handle the registration error here
          console.error('Registration failed:', response.statusText);
          return;
        }

        const json = response.json()
        sessionStorage.setItem('user', JSON.stringify(json) )
        // Check the user's role
        const router = useRouter();
        if (json.role === 'contractor') {
          // Redirect to the contractor-specific route
          await router.push({name: 'ContractorDashboard'}); // Replace with the actual route name
        } else {
          // Redirect to the general user route
          await router.push({name: 'UserDashboard'}); // Replace with the actual route name
        }

      } catch (error) {
        // Handle any network or other errors here
        console.error('An error occurred during registration:', error);
      }
    }
  }
});
</script>

<style scoped>
.register-container {
  background-color: var(--background-color);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px;
  margin: 0 auto;
}

.register-title {
  color: var(--primary-color);
  text-align: center;
}

.register-form {
  text-align: left;
}

.form-group {
  margin-bottom: 16px;
}

.form-label {
  color: var(--text-color);
  display: block;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: white;
  color: #333;
}

.form-input:focus {
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
  background-color: #0077b6;
}
</style>
