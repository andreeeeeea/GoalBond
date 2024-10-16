<template>
  <div class="flex flex-col items-center justify-center pt-14">
    <h1 class="text-2xl font-bold">Login</h1>
    <div class="w-96"> <!-- Added width to the container -->
      <form @submit.prevent="handleLogin" class="mt-10">
        <div class="mb-4">
          <input v-model="username" placeholder="Username" required class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <div class="mb-4">
          <input v-model="password" type="password" placeholder="Password" required class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <button type="submit" class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-500 transition duration-300">Login</button>
      </form>
      <div class="my-4">
          <p class="text-center">Don't have an account? <router-link to="/signup" class="text-blue-500">Sign Up</router-link></p>
      </div>
    </div>
    <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
  </div>
</template>


  <style scoped>
  </style>
  
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
    mounted() {
      if (this.$store.state.isAuthenticated) {
        this.$router.push('/');
      }
    },
  };
  </script>
  
  
  <style scoped>
  /* Add your styles here if needed */
  </style>

