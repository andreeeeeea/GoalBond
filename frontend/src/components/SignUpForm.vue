<template>
  <div class="items-center justify-center py-10 px-4">
    <div class="w-96 mx-auto py-32">
      <h2 class="text-2xl font-bold text-center">Sign Up</h2>
      <form @submit.prevent="addUser" class="mt-10">
        <div class="mb-4">
          <input 
            v-model="username" 
            type="text" 
            placeholder="Username" 
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <input 
            v-model="email" 
            type="email" 
            placeholder="Email" 
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <div class="mb-4">
          <input 
            v-model="password" 
            type="password" 
            placeholder="Password" 
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <button 
          type="submit"
          class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-500 transition duration-300"
        >
          Sign Up
        </button>
        <div v-if="successMessage" class="text-green-500 text-center mt-2">{{ successMessage }}</div>
        <div v-if="errorMessage" class="text-red-500 text-center mt-2">{{ errorMessage }}</div>
      </form>
      <div class="my-4">
          <p class="text-center">Already have an account? <router-link to="/login" class="text-blue-500">Log In</router-link></p>
      </div>
    </div>   
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    }
  },
  methods: {
    async addUser() {
      try {
        const response = await axios.post('http://localhost:5000/signup', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        console.log('User added:', response.data);
        this.successMessage = 'User successfully added!';
        
        // Clear input fields
        this.username = '';
        this.email = '';
        this.password = '';
        this.errorMessage = '';  // Clear error message if successful
        
        // Redirect to login page
        this.$router.push('/login');
      } catch (error) {
        console.error('Error adding user:', error);
        if (error.response && error.response.data) {
          this.errorMessage = error.response.data.message; // Set the error message returned from the backend
        } else {
          this.errorMessage = 'An unexpected error occurred. Please try again.'; // General error message
        }
      }
    }
  },
  mounted() {
    if (this.isAuthenticated) {
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>

