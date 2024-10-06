<template>
  <div>
    <div v-if="isAuthenticated" class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
      <h2 class="text-2xl font-semibold mb-4 text-center">Add Goal</h2>
      <form @submit.prevent="addGoal">
        <div class="mb-4">
          <input
            v-model="title"
            type="text"
            placeholder="Goal Title"
            required
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>
        <div class="mb-4">
          <textarea
            v-model="description"
            placeholder="Description"
            class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          ></textarea>
        </div>
        <button
          type="submit"
          class="w-full bg-green-600 text-white font-bold py-2 rounded-lg hover:bg-green-500 transition duration-300"
        >
          Add Goal
        </button>
      </form>
    </div>

    <div v-else class="text-center mt-10">
      <p>You must be logged in to add a goal.</p>
      <router-link to="/login" class="text-blue-500">Log In</router-link>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default {
  setup() {
    const store = useStore();
    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const title = ref('');
    const description = ref('');

    const addGoal = async () => {
      if (!isAuthenticated.value) {
        alert('You must be logged in to add a goal.');
        return;
      }

      try {
        const response = await axios.post('http://localhost:5000/goals', {
          title: title.value,
          description: description.value,
          // Do not send user_id here
        });
        console.log('Goal added:', response.data);
        title.value = '';
        description.value = '';
      } catch (error) {
        console.error('Error adding goal:', error.response.data);
      }
    };

    return {
      isAuthenticated,
      title,
      description,
      addGoal,
    };
  },
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
