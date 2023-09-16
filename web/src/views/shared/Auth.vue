<template>
  <div>
    <div>
      <button @click="activeTab = 'login'">Login</button>
      <button @click="activeTab = 'register'">Register</button>
    </div>

    <div v-if="activeTab === 'login'">
      <input v-model="loginEmail" placeholder="Email" /><br>
      <input type="password" v-model="loginPassword" placeholder="Password" /><br>
      <button @click="login">Login</button>
    </div>

    <div v-if="activeTab === 'register'">
      <input v-model="registerName" placeholder="Name" /><br>
      <input v-model="registerEmail" placeholder="Email" /><br>
      <input type="password" v-model="registerPassword" placeholder="Password" /><br>
      <input type="password" v-model="confirmPassword" placeholder="Confirm Password" /><br>
      <button @click="register">Register</button>
      <div v-if="passwordMismatch" style="color: red;">Passwords do not match</div>
    </div><br>

    <div v-if="errorMessage" style="color: red;">
      {{ errorMessage }}
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  data() {
    return {
      activeTab: 'login',
      loginEmail: '',
      loginPassword: '',
      registerName: '',
      registerEmail: '',
      registerPassword: '',
      registerRole: 'user',
      confirmPassword: '',
      passwordMismatch: false,
      errorMessage: ''
    };
  },
  setup() {
    const router = useRouter();
    return { router };
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
      try {
        const response = await axios.post('http://localhost:3000/v1/users/login', {
          email: this.loginEmail,
          password: this.loginPassword,
        }, {
          timeout: 5000
        });

        console.log('Login successful', response.data);

        if (response.data.role === 'user') {
          this.router.push('/user/dashboard');
        } else if (response.data.role === 'contractor') {
          this.router.push('/contractor/dashboard');
        }
      } catch (error) {
        console.error('Login failed', error);
        if (error.code === 'ECONNABORTED') {
          this.errorMessage = 'The connection to the database timed out. Please try again later.';
        } else {
          this.errorMessage = 'An error occurred while logging in. Please try again.';
        }
      }
    },
    async register() {
      if (this.passwordMismatch) {
        return;
      }

      try {
        const response = await axios.post('http://localhost:3000/v1/users/register', {
          name: this.registerName,
          email: this.registerEmail,
          password: this.registerPassword,
          role: this.registerRole,
        }, {
          timeout: 5000
        });

        console.log('Registration successful', response.data);

        if (response.data.role === 'user') {
          this.router.push('/user/dashboard');
        } else if (response.data.role === 'contractor') {
          this.router.push('/contractor/dashboard');
        }
      } catch (error) {
        console.error('Registration failed', error);
        if (error.code === 'ECONNABORTED') {
          this.errorMessage = 'The connection to the database timed out. Please try again later.';
        } else {
          this.errorMessage = 'An error occurred while registering. Please try again.';
        }
      }
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
