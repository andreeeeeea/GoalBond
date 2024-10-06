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
          await this.login({ username: this.username, password: this.password });
          this.$router.push('/'); // Redirect to home on successful login
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
