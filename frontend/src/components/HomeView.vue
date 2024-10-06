<template>
  <div class="home-view">
    <h1 class="text-3xl font-bold mb-4">Welcome to the Home View</h1>
    <p class="text-gray-700">
      <span v-if="isAuthenticated">Hello, {{ username }}!</span>
      <span v-else>Hello, random person! Log in to see your goals!</span>
    </p>
    <p class="text-gray-700">This is the home view where you can track your goals!</p>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'HomeView',
  setup() {
    const store = useStore();
    
    // Use computed to access the authentication state and username from Vuex store
    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || ''); // Ensure username is a string

    return {
      isAuthenticated,
      username,
    };
  },
};
</script>

<style scoped>
/* Add your styles here if needed */
</style>
