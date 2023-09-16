<template>
  <div>
    <h1 style="color: var(--primary-color);">Register Vue</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username" style="color: var(--text-color);">Username:</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div>
        <label for="email" style="color: var(--text-color);">Email:</label>
        <input type="email" id="email" v-model="email" />
      </div>
      <div>
        <label for="password" style="color: var(--text-color);">Password:</label>
        <input type="password" id="password" v-model="password" />
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import {useRouter} from "vue-router";

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
        if (json.role === 'contractor') {
          // Redirect to the contractor-specific route
          const router = useRouter();
          router.push({ name: 'ContractorDashboard'}); // Replace with the actual route name
        } else {
          // Redirect to the general user route
          const router = useRouter();
          router.push({ name: 'UserDashboard' }); // Replace with the actual route name
        }

      } catch (error) {
        // Handle any network or other errors here
        console.error('An error occurred during registration:', error);
      }
    }
  }
});
</script>
