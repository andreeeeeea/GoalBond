<template>
  <div class="items-center justify-center py-12 px-4">
    <div class="w-96 mx-auto py-32">
      <h1 class="text-2xl font-bold text-center">Forgot Password</h1>
      <form @submit.prevent="sendResetLink" class="mt-10">
        <div class="mb-4">
          <label for="email" class="block">Enter your email address:</label>
          <input 
            type="email" 
            v-model="email" 
            :disabled="loading"
            required 
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052] disabled:opacity-50" 
          />
        </div>
        <button 
          type="submit" 
          :disabled="loading"
          class="w-full bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg hover:bg-[#8B2440] transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {{ loading ? 'Sending...' : 'Send Reset Link' }}
        </button>
      </form>
      <div class="my-4">
        <p class="text-center">Don't have an account? <router-link to="/signup" class="text-[#B03052] hover:text-[#8B2440]">Sign Up</router-link></p>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';  // Import axios
  import { useToast } from 'vue-toastification';
  
  export default {
    setup() {
      const toast = useToast();
      return { toast };
    },
    data() {
      return {
        email: '',
        loading: false,
      };
    },
    methods: {
      async sendResetLink() {
        this.loading = true;
        try {
          const response = await axios.post('/forgot_password', {
            email: this.email
          });
  
          if (response.data.success) {
            this.toast.success('Password reset link has been sent to your email. Please check your inbox.');
            this.email = '';  // Clear the form
            // Optionally redirect to login after a delay
            setTimeout(() => {
              this.$router.push('/login');
            }, 3000);
          } else {
            this.toast.error(response.data.message || 'Failed to send reset link.');
          }
        } catch (error) {
          console.error("Error sending reset link:", error); 
          this.toast.error(error.response?.data?.message || 'An error occurred. Please try again.');
        } finally {
          this.loading = false;
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
  