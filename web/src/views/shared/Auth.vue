<template>
  <div>
    <div class="tabs">
      <button :class="{ active: activeTab === 'login' }" @click="activeTab = 'login'">Login</button>
      <button :class="{ active: activeTab === 'register' }" @click="activeTab = 'register'">Register</button>
    </div>
    <div class="tab-content">
      <div v-if="activeTab === 'login'">
        <h2>Login</h2>
        <form @submit.prevent="login">
          <div>
            <label>Email: </label>
            <input type="email" v-model="loginEmail" required />
          </div>
          <div>
            <label>Password: </label>
            <input type="password" v-model="loginPassword" required />
          </div>
          <button type="submit">Login</button>
        </form>
      </div>
      <div v-if="activeTab === 'register'">
        <h2>Register</h2>
        <form @submit.prevent="register">
          <div>
            <label>Name: </label>
            <input type="text" v-model="registerName" required />
          </div>
          <div>
            <label>Email: </label>
            <input type="email" v-model="registerEmail" required />
          </div>
          <div>
            <label>Password: </label>
            <input type="password" v-model="registerPassword" required />
          </div>
          <div>
            <label>Confirm Password: </label>
            <input type="password" v-model="confirmPassword" required />
          </div>
          <div v-if="passwordMismatch" style="color: red;">
            Passwords do not match
          </div>
          <div>
            <label>Role: </label>
            <input type="text" v-model="registerRole" required />
          </div>
          <button type="submit" :disabled="passwordMismatch">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeTab: 'login',
      loginEmail: '',
      loginPassword: '',
      registerName: '',
      registerEmail: '',
      registerPassword: '',
      registerRole: '',
      confirmPassword: '',
      passwordMismatch: false,
    };
  },
  watch: {
    registerPassword() {
      this.checkPasswordMatch();
    },
    confirmPassword() {
      this.checkPasswordMatch();
    },
  },
  methods: {
    checkPasswordMatch() {
      this.passwordMismatch = this.registerPassword !== this.confirmPassword;
    },
    async login() {
      // ... Existing login method
    },
    async register() {
      if (this.passwordMismatch) {
        return;
      }

      // ... Existing register method
    },
  },
};
</script>

<style>
.tabs {
  display: flex;
  margin-bottom: 20px;
}
.tabs button {
  flex: 1;
  padding: 10px;
}
.tabs button.active {
  background-color: #f0f0f0;
}
.tab-content {
  border: 1px solid #ccc;
  padding: 20px;
}
</style>
