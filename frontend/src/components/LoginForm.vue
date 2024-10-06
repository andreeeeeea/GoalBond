<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="Username" required />
        <input v-model="password" type="password" placeholder="Password" required />
        <button type="submit">Login</button>
      </form>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
      };
    },
    methods: {
      ...mapActions(['login']),
      async handleLogin() {
        try {
          // Ignore response data
          await axios.post('http://localhost:5000/login', {
            username: this.username,
            password: this.password,
          });
          
          // Assuming the user object structure based on successful login
          const userData = { username: this.username }; // Use username for simplicity
          this.login(userData); // Commit user data to Vuex
          this.$router.push('/'); // Redirect to home
        } catch (error) {
          this.errorMessage = 'Invalid username or password';
        }
      },
    },
  };
  </script>
  
  
  <style scoped>
  /* Add your styles here if needed */
  </style>
  