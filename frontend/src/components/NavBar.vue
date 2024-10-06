<template>
  <nav class="flex justify-between items-center bg-gray-400 px-4 py-2">
    <router-link to="/" class="text-xl">My Goals App</router-link>
    <div class="flex items-center space-x-4"> <!-- Flex container for items -->
      <span class="text-white">
        <!-- Display username if authenticated, else display default message -->
        {{ isAuthenticated ? `Hello, ${username}!` : 'Hello, random person!' }}
      </span>
      <button v-if="!isAuthenticated" @click="goToLogin" class="px-4 py-2 rounded">Login</button>
      <button v-if="!isAuthenticated" @click="goToSignup" class="px-4 py-2 rounded">Sign Up</button>
      <button v-if="isAuthenticated" @click="logout" class="text-white bg-red-500 hover:bg-red-600 px-4 py-2 rounded">Logout</button>
    </div>
  </nav>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'; 

export default {
  setup() {
    const store = useStore();
    const router = useRouter(); 

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || ''); // Ensure username is a string

    const logout = () => {
      store.dispatch('logout');
      // Optionally, call your backend logout endpoint
      // fetch('http://localhost:5000/logout', { method: 'POST' });
    };

    const goToLogin = () => {
      router.push('/login');
    };

    const goToSignup = () => {
      router.push('/signup');
    };

    return {
      isAuthenticated,
      username,
      logout,
      goToLogin,
      goToSignup,
    };
  },
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
