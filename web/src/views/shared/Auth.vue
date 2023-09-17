<template>
  <div>
    <div class="tabs">
      <button :class="{ active: activeTab === 'login' }" @click="activeTab = 'login'" class="tab-button">Login</button>
      <button :class="{ active: activeTab === 'register' }" @click="activeTab = 'register'" class="tab-button">Register</button>
    </div>
    <div class="tab-content">
      <div v-if="activeTab === 'login'" class="tab-pane" >
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
      try {
        const response = await axios.post('http://localhost:4000/api/user/login', {
          email: this.loginEmail,
          password: this.loginPassword,
        }, {
          timeout: 5000
        });
        sessionStorage.setItem('user', JSON.stringify(response.data))
        console.log('Login successful', response.data);
        const router = this.$router
        if (response.data.role === 'user') {
          await router.push('/user/dashboard');
        } else if (response.data.role === 'contractor') {
          await router.push('/contractor/dashboard');
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
        const response = await axios.post('http://localhost:4000/api/user/signup', {
          name: this.registerName,
          email: this.registerEmail,
          password: this.registerPassword,
          role: this.registerRole,
        }, {
          timeout: 5000
        });

        console.log('registration successful', response.data);
        sessionStorage.setItem('user', JSON.stringify(response.data))

        const router = this.$router

        if (response.data.role === 'user') {
           await router.push('/user/dashboard');
        } else if (response.data.role === 'contractor') {
          await router.push('/contractor/dashboard');
        }
      } catch (error) {
        console.error('registration failed', error);
        if (error.code === 'ECONNABORTED') {
          this.errorMessage = 'The connection to the database timed out. Please try again later.';
        } else {
          this.errorMessage = 'An error occurred while logging in. Please try again.';
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

.tab-button {
flex: 1;
padding: 10px;
background-color: var(--background-color);
border: 1px solid #ccc;
cursor: pointer;
text-align: center;
color: var(--primary-color);
font-weight: bold;
}

.tab-button.active {
background-color: var(--accent-color);
color: white;
}

.tab-content {
border: 1px solid #ccc;
padding: 20px;
background-color: var(--background-color);
border-radius: 8px;
}

.tab-pane {
flex-direction: column; /* Set the flex direction to column for alignment */
}

.tab-pane h2 {
color: var(--primary-color);
margin-bottom: 20px;
}

/* Show the active tab pane */
.tab-pane.active {
display: flex;
}

/* Label style */
.label {
width: 150px; /* Set a fixed width for labels */
margin-right: 10px;
text-align: right; /* Align the labels to the right */
font-weight: bold;
}

/* Input field style */
.input-field {
flex: 1;
border: 1px solid #ccc;
padding: 8px;
border-radius: 4px;
margin-bottom: 10px;
}

/* Error message style */
.error-message {
color: red;
margin-top: 10px;
}
</style>