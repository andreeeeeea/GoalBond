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
      </form>
      <div class="my-4">
          <p class="text-center">Already have an account? <router-link to="/login" class="text-blue-500">Log In</router-link></p>
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

