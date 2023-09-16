<template>
  <div class="login-container">
    <h1 class="login-title">Login Vue</h1>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="email" class="form-label">Email:</label>
        <input type="text" id="email" v-model="email" class="form-input" />
      </div>
      <div class="form-group">
        <label for="password" class="form-label">Password:</label>
        <input type="password" id="password" v-model="password" class="form-input" />
      </div>
      <div class="form-group">
        <button type="submit" class="login-button">Login</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRouter } from "vue-router";

export default defineComponent({
  name: 'LoginVue',

  data() {
    return {
      email: '',
      password: '',
    };
  },

  methods: {
    async login() {
      // Construct the login data
      const loginData = {
        email: this.email,
        password: this.password,
      };

      try {
        const response = await fetch('/api/users/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(loginData),
        });

        if (!response.ok) {
          // Handle the login error here
          console.error('Login failed:', response.statusText);
          return;
        }

        const json = await response.json();
        sessionStorage.setItem('user', JSON.stringify(json));
        // Check the user's role
        const router = useRouter();
        if (json.role === 'contractor') {
          // Redirect to the contractor-specific route
          await router.push({ name: 'ContractorDashboard' }); // Replace with the actual route name
        } else {
          // Redirect to the general user route
          await router.push({ name: 'UserDashboard' }); // Replace with the actual route name
        }
        console.log('Login successful');
      } catch (error) {
        // Handle any network or other errors here
        console.error('An error occurred during login:', error);
      }
    },
  },
});
</script>

<style scoped>
.login-container {
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: var(--background-color);
}

.login-title {
  font-size: 24px;
  margin-bottom: 20px;
  color: var(--primary-color);
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  margin-bottom: 20px; /* Increased spacing between form groups */
}

.form-label {
  color: var(--text-color); /* Text color for labels */
}

.form-input {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 4px;
  width: 100%;
  margin-top: 5px; /* Adjusted margin for input fields */
}

.login-button {
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
  background-color: var(--accent-color);
  color: white;
}

.login-button:hover {
  background-color: #0077b6;
}
</style>
