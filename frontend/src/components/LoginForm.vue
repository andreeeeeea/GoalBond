<template>
  <div class="items-center justify-center py-12 px-4">
    <div class="w-96 mx-auto pt-32">
      <h1 class="text-2xl font-bold text-center">Login</h1>
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
          <p class="text-center">Forgot your password? <router-link to="/forgot_password" class="text-blue-500">Reset Password</router-link></p>
      </div>
    </div>
  </div>
</template>


  <style scoped>
  </style>
  
  <script>
  import { mapActions } from 'vuex';
  import { useToast } from 'vue-toastification';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      ...mapActions(['login']),
      async handleLogin() {
        try {
          await this.login({ username: this.username, password: this.password });
          this.$router.push('/'); 
          this.toast.success('Login successful');
        } catch (error) {
          this.toast.error('Invalid username or password');
        }
      },
    },
    async mounted() {
      this.toast = useToast();
      if (this.$store.state.isAuthenticated) {
        this.$router.push('/');
      }
    },
  };
  </script>
  
  
  <style scoped>
  </style>

