<template>
  <div class="login-container">
    <h1 class="login-title">Login Vue</h1>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="username" class="form-label">Username:</label>
        <input type="text" id="username" v-model="username" class="form-input" />
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
export default defineComponent({
  name: 'LoginVue',

  data() {
    return {
      username: '',
      password: '',
    };
  },

  methods: {
    login() {
      // Perform authentication logic here
      // For this example, we'll emit an event with the entered username
      this.$emit('login', this.username);
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
