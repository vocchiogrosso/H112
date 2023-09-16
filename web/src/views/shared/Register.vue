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
import { defineComponent, ref } from 'vue';

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
    register() {
      // Perform registration logic here
      // For this example, we'll emit an event with the entered username
      this.$emit('register', this.username);
    },
  },
});
</script>
