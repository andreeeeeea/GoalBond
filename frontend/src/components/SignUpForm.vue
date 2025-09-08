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
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
            required
          />
        </div>
        <div class="mb-4">
          <input 
            v-model="email" 
            type="email" 
            placeholder="Email" 
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
            required
          />
        </div>
        <div class="mb-4">
          <input 
            v-model="password" 
            type="password" 
            placeholder="Password" 
            @input="validatePassword"
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052]"
            required
          />
          <div v-if="passwordErrors.length > 0" class="mt-2">
            <p class="text-xs text-red-500" v-for="error in passwordErrors" :key="error">{{ error }}</p>
          </div>
          <div v-if="password && passwordErrors.length === 0" class="mt-2">
            <p class="text-xs text-green-500">✓ Password meets all requirements</p>
          </div>
          <div v-if="!password" class="mt-2 text-xs text-gray-500">
            <p class="font-semibold mb-1">Password must contain:</p>
            <ul class="list-disc list-inside space-y-0.5">
              <li>At least 8 characters</li>
              <li>At least one uppercase letter</li>
              <li>At least one number</li>
              <li>At least one symbol (!@#$%^&*)</li>
            </ul>
          </div>
        </div>
        <button 
          type="submit"
          :disabled="passwordErrors.length > 0"
          class="w-full bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg hover:bg-[#8B2440] transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          Sign Up
        </button>
      </form>
      <div class="my-4">
          <p class="text-center">Already have an account? <router-link to="/login" class="text-[#B03052]">Log In</router-link></p>
      </div>
    </div>   
  </div>
</template>


<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      passwordErrors: [],
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    }
  },
  methods: {
    validatePassword() {
      this.passwordErrors = [];
      
      if (this.password.length < 8) {
        this.passwordErrors.push('• Password must be at least 8 characters long');
      }
      
      if (!/[A-Z]/.test(this.password)) {
        this.passwordErrors.push('• Password must contain at least one uppercase letter');
      }
      
      if (!/[0-9]/.test(this.password)) {
        this.passwordErrors.push('• Password must contain at least one number');
      }
      
      if (!/[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?]/.test(this.password)) {
        this.passwordErrors.push('• Password must contain at least one symbol');
      }
    },
    async addUser() {
      // Validate password before submitting
      this.validatePassword();
      
      if (this.passwordErrors.length > 0) {
        this.toast.error('Please fix password errors before submitting');
        return;
      }
      
      try {
        const response = await axios.post('/signup', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        console.log('User added:', response.data);
        
        // Clear input fields
        this.username = '';
        this.email = '';
        this.password = '';
        this.passwordErrors = [];
        
        // Redirect to login page
        this.$router.push('/login');
        this.toast.success('Successfully signed up! Please log in.');
      } catch (error) {
        console.error('Error adding user:', error);
        this.toast.error('Error signing up. Please try again.');
        if (error.response && error.response.data) {
          this.toast.error(error.response.data.message);
        } else {
          this.toast.error('Error signing up. Please try again.');
        }
      }
    }
  },
  mounted() {
    this.toast = useToast();
    if (this.isAuthenticated) {
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>

