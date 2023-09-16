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
import "../../style.css"
import {useRouter} from "vue-router";
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
        // Construct the registration data
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
            // Handle the registration error here
            console.error('Registration failed:', response.statusText);
            return;
          }

          const json = response.json()
          sessionStorage.setItem('user', JSON.stringify(json) )
          // Check the user's role
          if (json.role === 'contractor') {
            // Redirect to the contractor-specific route
            const router = useRouter();
            router.push({ name: 'ContractorDashboard'}); // Replace with the actual route name
          } else {
            // Redirect to the general user route
            const router = useRouter();
            router.push({ name: 'UserDashboard' }); // Replace with the actual route name
          }
          console.log('Registration successful');
        } catch (error) {
          // Handle any network or other errors here
          console.error('An error occurred during registration:', error);
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
}

.login-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-group {
  margin-bottom: 10px;
}

.form-label {
  font-weight: bold;
}

.form-input {
  border: none;
  padding: 8px;
  border-radius: 4px;
}

.login-button {
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

</style>
