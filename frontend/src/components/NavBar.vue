<template>
  <nav class="flex justify-between items-center bg-gray-800 px-6 py-4 shadow-lg">
    <!-- App name -->
    <router-link to="/" class="text-2xl font-bold text-white hover:text-indigo-400 transition-colors duration-300">
      GoalBond
    </router-link>

    <!-- Right-side controls -->
    <div class="flex items-center space-x-6">
      <!-- Greeting message -->
       <span v-if="isAuthenticated" class="text-gray-300 text-lg">
        Hello, {{ username }}!
      </span>

      <!-- Authentication buttons -->
      <div class="space-x-4">
        <button
          v-if="!isAuthenticated"
          @click="goToLogin"
          class="text-white bg-indigo-600 hover:bg-indigo-700 px-5 py-2 rounded-full shadow-md transition-all duration-300"
        >
          Login
        </button>
        <button
          v-if="!isAuthenticated"
          @click="goToSignup"
          class="text-white bg-indigo-500 hover:bg-indigo-600 px-5 py-2 rounded-full shadow-md transition-all duration-300"
        >
          Sign Up
        </button>
        <button
          v-if="isAuthenticated"
          @click="logout"
          class="text-white bg-red-500 hover:bg-red-600 px-5 py-2 rounded-full shadow-md transition-all duration-300"
        >
          Logout
        </button>
        <button
          v-if="isAuthenticated"
          @click="goToGoals"
          class="text-white bg-green-500 hover:bg-green-600 px-5 py-2 rounded-full shadow-md transition-all duration-300"
        >
          My Goals
        </button>
        <button
          v-if="isAuthenticated"
          @click="goToGroups"
          class="text-white bg-yellow-500 hover:bg-yellow-600 px-5 py-2 rounded-full shadow-md transition-all duration-300"
        >
          Groups
        </button>
      </div>
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
    const username = computed(() => store.getters.getUsername || '');

    const logout = async () => {
      await store.dispatch('logout');
      router.push('/login');
    };

    const goToLogin = () => {
      router.push('/login');
    };

    const goToSignup = () => {
      router.push('/signup');
    };

    const goToGoals = () => {
      router.push('/goals');
    };

    const goToGroups = () => {
      router.push('/groups');
    };

    return {
      isAuthenticated,
      username,
      logout,
      goToLogin,
      goToSignup,
      goToGoals,
      goToGroups,
    };
  },
};
</script>

<style scoped>
nav {
  font-family: 'Inter', sans-serif;
}
</style>
