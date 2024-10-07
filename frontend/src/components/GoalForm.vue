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
        <div class="mb-4">
          <input type="checkbox" id="hasDeadline" v-model="hasDeadline" />
          <label for="hasDeadline">Add Deadline?</label>
        </div>
        <div v-if="hasDeadline" class="mb-4">
          <label for="deadline">Deadline:</label>
          <input type="datetime-local" id="deadline" v-model="deadline" required />
        </div>
        <button
          type="submit"
          class="w-full bg-green-600 text-white font-bold py-2 rounded-lg hover:bg-green-500 transition duration-300"
        >
          Add Goal
        </button>
        <p v-if="successMessage" class="text-green-500 mt-2">{{ successMessage }}</p>
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
    const hasDeadline = ref(false);
    const deadline = ref('');
    const successMessage = ref('');

    const addGoal = async () => {
      if (!isAuthenticated.value) {
        alert('You must be logged in to add a goal.');
        return;
      }

      try {
        const response = await axios.post('http://localhost:5000/goals', {
          title: title.value,
          description: description.value,
          deadline: hasDeadline.value ? new Date(deadline.value).toISOString() : null, // Handle deadline
          dateAdded: new Date().toISOString(), // Optionally include date added
        });
        console.log('Goal added:', response.data);

        // Set success message
        successMessage.value = 'Goal successfully added!';

        // Clear the input fields
        title.value = '';
        description.value = '';
        deadline.value = '';
        hasDeadline.value = false; // Reset the hasDeadline state
      } catch (error) {
        console.error('Error adding goal:', error.response.data);
        successMessage.value = ''; // Clear success message on error
      }
    };

    return {
      isAuthenticated,
      title,
      description,
      hasDeadline,
      deadline,
      successMessage,
      addGoal,
    };
  },
};
</script>

<style scoped>
/* Add any additional styles if needed */
</style>
