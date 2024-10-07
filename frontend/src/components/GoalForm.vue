<template>
  <div>
    <div v-if="isAuthenticated" class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
      <h2 class="text-2xl font-semibold mb-4 text-center">Add Goal</h2>
      <form @submit.prevent="addGoal">
        <div class="mb-4">
          <label>
            <input type="radio" v-model="goalType" value="personal" /> Personal Goal
          </label>
          <label class="ml-4">
            <input type="radio" v-model="goalType" value="group" /> Group Goal
          </label>
        </div>

        <div v-if="goalType === 'group'" class="mb-4">
          <select v-model="selectedGroup" class="w-full p-2 border border-gray-300 rounded-lg">
            <option disabled value="">Select a Group</option>
            <option v-for="group in groups" :key="group.id" :value="group.id">{{ group.name }}</option>
          </select>
        </div>

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
          <input type="date" id="deadline" v-model="deadline" required />
        </div>
        <button
          type="submit"
          class="w-full bg-green-600 text-white font-bold py-2 rounded-lg hover:bg-green-500 transition duration-300"
        >
          Add Goal
        </button>
        <p v-if="successMessage" class="text-green-500 mt-2">{{ successMessage }}</p>
        <p v-if="errorMessage" class="text-red-500 mt-2">{{ errorMessage }}</p>
      </form>
    </div>

    <div v-else class="text-center mt-10">
      <p>You must be logged in to add a goal.</p>
      <router-link to="/login" class="text-blue-500">Log In</router-link>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
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
    const errorMessage = ref('');
    const selectedGroup = ref('');
    const groups = ref([]);
    const goalType = ref('personal'); // New ref to store the type of goal

    onMounted(async () => {
      try {
        const response = await axios.get('http://localhost:5000/groups');
        groups.value = response.data;
      } catch (error) {
        console.error('Error fetching groups:', error);
      }
    });

    const addGoal = async () => {
      if (!isAuthenticated.value) {
        alert('You must be logged in to add a goal.');
        return;
      }

      const url = goalType.value === 'group'
        ? `http://localhost:5000/groups/${selectedGroup.value}/goals`
        : 'http://localhost:5000/goals'; // Change to the personal goals endpoint

      try {
        const response = await axios.post(url, {
          title: title.value,
          description: description.value,
          deadline: hasDeadline.value ? new Date(deadline.value).toISOString() : null,
          // For personal goals, you might want to include user_id or other details if needed
        });
        console.log('Goal added:', response.data);

        successMessage.value = goalType.value === 'group'
          ? 'Group goal successfully added!'
          : 'Personal goal successfully added!';
        errorMessage.value = '';

        // Clear input fields
        title.value = '';
        description.value = '';
        deadline.value = '';
        hasDeadline.value = false;
        selectedGroup.value = ''; // Reset selected group
      } catch (error) {
        console.error('Error adding goal:', error.response.data);
        successMessage.value = '';
        errorMessage.value = error.response.data.message || 'An error occurred while adding the goal.';
      }
    };

    return {
      isAuthenticated,
      title,
      description,
      hasDeadline,
      deadline,
      successMessage,
      errorMessage,
      selectedGroup,
      groups,
      goalType,
      addGoal,
    };
  },
};
</script>
