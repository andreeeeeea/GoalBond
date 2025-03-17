<template>
  <div class="items-center justify-center py-12 px-4">
    <div class="w-96 mx-auto py-32">
      <h1 class="text-2xl font-bold text-center">Forgot Password</h1>
      <form @submit.prevent="sendResetLink" class="mt-10">
        <div class="mb-4">
          <label for="email" class="block">Enter your email address:</label>
          <input type="email" v-model="email" required class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <button type="submit" class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-500 transition duration-300">Send Reset Link</button>
      </form>
      <div class="my-4">
        <p class="text-center">Don't have an account? <router-link to="/signup" class="text-blue-500">Sign Up</router-link></p>
        <p v-if="message" :class="messageClass" class="mt-2 text-center">{{ message }}</p>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';  // Import axios
  
  export default {
    data() {
      return {
        email: '',
        message: '',
        messageClass: ''
      };
    },
    methods: {
      async sendResetLink() {
        try {
          console.log(`Sending reset link for email: ${this.email}`); 
  
          const response = await axios.post('/forgot_password', {
            email: this.email
          });
  
          console.log(`Response from server:`, response.data); 
  
          this.message = response.data.message;
          this.messageClass = response.data.success ? 'success' : 'error';
        } catch (error) {
          console.error("Error sending reset link:", error); 
          this.message = 'An error occurred. Please try again.';
          this.messageClass = 'error';
        }
      }
    }
  };
  </script>
  
  <style>
  .success {
    color: green;
  }
  
  .error {
    color: red;
  }
  </style>
  