<template>
  <header class="bg-white shadow">
    <div class="container mx-auto flex justify-between items-center p-4">
      <!-- App name -->
      <router-link to="/" class="text-2xl font-bold text-gray-800 hover:text-indigo-600 transition-colors duration-300">
        GoalBond
      </router-link>

      <!-- Right-side controls -->
      <div class="flex items-center space-x-6">
      <!-- Authentication buttons -->
        <div class="flex items-center space-x-4">
          <button
            v-if="!isAuthenticated"
            @click="goToLogin"
            class="text-xl text-gray-600 px-4 py-2 rounded transition duration-300"
          >
            Login
          </button>
          <button
            v-if="!isAuthenticated"
            @click="goToSignup"
            class="text-xl text-gray-600  px-4 py-2 rounded transition duration-300"
          >
            Sign Up
          </button>

          <button
            v-if="isAuthenticated"
            @click="goToGoals"
            class="text-xl text-gray-600 px-4 py-2 rounded transition duration-300"
          >
            Goals
          </button>
          <button
            v-if="isAuthenticated"
            @click="goToGroups"
            class="text-xl text-gray-600 px-4 py-2 rounded transition duration-300"
          >
            Groups
          </button>
          <button
            v-if="isAuthenticated"
            @click="goToAccount"
            class="text-xl text-gray-600  px-4 py-2 rounded transition duration-300"
          >
            Account
          </button>
        </div>
      </div>
    </div>
  </header>
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

    const goToAccount = () => {
      router.push('/account');
    };

    return {
      isAuthenticated,
      username,
      goToLogin,
      goToSignup,
      goToGoals,
      goToGroups,
      goToAccount,
    };
  },
};
</script>

<style scoped>
nav {
  font-family: 'Inter', sans-serif;
}
</style>
