<template>
  <div v-if="!isAuthenticated" class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
    <h2 class="text-2xl font-semibold mb-4 text-center">User Sign Up</h2>
    <form @submit.prevent="addUser" class="space-y-4">
      <div>
        <input 
          v-model="username" 
          type="text" 
          placeholder="Username" 
          class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>
      <div>
        <input 
          v-model="email" 
          type="email" 
          placeholder="Email" 
          class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>
      <div>
        <input 
          v-model="password" 
          type="password" 
          placeholder="Password" 
          class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>
      <button 
        type="submit"
        class="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-500 transition duration-200"
      >
        Add User
      </button>
      <div v-if="successMessage" class="text-green-500 text-center mt-2">{{ successMessage }}</div>
      <div v-if="errorMessage" class="text-red-500 text-center mt-2">{{ errorMessage }}</div>
    </form>
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

