<template>
  <div v-if="isAuthenticated" class="mx-4">
    <!-- Button to Toggle Form Visibility -->
    <div class="text-center mt-10">
      <button
        @click="showForm = !showForm"
        class="bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-500 transition duration-300"
      >
        {{ showForm ? 'Cancel' : 'Add Goal' }}
      </button>
    </div>

    <!-- Add Goal Section -->
    <div v-if="showForm" class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md mt-4">
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
          <label for="category">Category:</label>
          <select v-model="category" id="category" class="w-full p-2 border border-gray-300 rounded-lg">
            <option disabled value="">Select a Category</option>
            <option value="Books">Books</option>
            <option value="Coding">Coding</option>
            <option value="Cooking">Cooking</option>
            <option value="Fitness">Fitness</option>
            <option value="Food and Dining">Food and Dining</option>
            <option value="Movies">Movies/Series</option>
            <option value="Music">Music</option>
            <option value="Photography">Photography</option>
            <option value="Travel">Travel</option>
            <option value="Other">Other</option>
          </select>
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


    <!-- Section for Personal Goals -->
    <div @click="showPersonalGoals = !showPersonalGoals" class="flex justify-between items-center cursor-pointer p-2 bg-gray-200 rounded-md mt-4">
      <h2 class="text-xl font-semibold">Personal Goals</h2>
      <span :class="['transition-transform', showPersonalGoals ? 'rotate-180' : '']">▼</span>
    </div>
    <div v-if="showPersonalGoals">
      <div v-if="personalGoals.length > 0" class="grid grid-cols-4 md:grid-cols-4 gap-4">
        <div v-for="goal in personalGoals" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-56">
          <div class="flex-grow">
            <p class="text-lg font-semibold">{{ goal.title }}</p>
            <p>{{ goal.description }}</p>
            <p> Category: {{ goal.category }}</p>
            <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
            <p>Status: To Do</p>
          </div>
          <div class="mt-auto">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
            <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
          </div>
        </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>No personal goals found.</p>
      </div>
    </div>

    <!-- Section for Group Goals -->
    <div @click="showGroupGoals = !showGroupGoals" class="flex justify-between items-center cursor-pointer p-2 bg-gray-200 rounded-md mt-4">
      <h2 class="text-xl font-semibold">Group Goals</h2>
      <span :class="['transition-transform', showGroupGoals ? 'rotate-180' : '']">▼</span>
    </div>
    <div v-if="showGroupGoals">
      <div v-if="groupGoals.length > 0" class="grid grid-cols-4 md:grid-cols-4 gap-4">
        <div v-for="goal in groupGoals" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-56">
          <div class="flex-grow">
            <h3 class="text-lg font-semibold">{{ goal.title }}</h3>
            <p>{{ goal.description }}</p>
            <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
            <p> Category: {{ goal.category }}</p>
            <p>Status: To Do</p>
            <p>Group: {{ goal.group.name }}</p>
            <p>Members: 
              <span v-for="member in goal.group.members" :key="member.id">{{ member.username }}<span v-if="!$last">, </span></span>
            </p>
          </div>
          <div class="mt-auto">
            <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
            <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
          </div>
        </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>No group goals found.</p>
      </div>
    </div>

    <!-- Section for Completed Goals -->
    <div @click="showCompletedGoals = !showCompletedGoals" class="flex justify-between items-center cursor-pointer p-2 bg-gray-200 rounded-md mt-4">
      <h2 class="text-xl font-semibold">Completed Goals</h2>
      <span :class="['transition-transform', showCompletedGoals ? 'rotate-180' : '']">▼</span>
    </div>
    <div v-if="showCompletedGoals">
      <div v-if="completedGoals.length > 0" class="grid grid-cols-4 md:grid-cols-4 gap-4">
        <div v-for="goal in completedGoals" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-56">
          <div class="flex-grow">
            <h3 class="text-lg font-semibold">{{ goal.title }}</h3>
            <p>{{ goal.description }}</p>
            <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
            <p> Category: {{ goal.category }}</p>
            <p>Status: Completed</p>
            <p v-if="goal.is_group_goal">Group: {{ goal.group.name }}</p>
            <p v-if="goal.is_group_goal">Members: 
              <span v-for="member in goal.group.members" :key="member.id">{{ member.username }}<span v-if="!$last">, </span></span>
            </p>
          </div>
          <div class="mt-auto">
            <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Re-do Goal</button>
            <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
          </div>
      </div>
      </div>
      <div v-else class="text-center mt-4">
        <p>No completed goals found.</p>
      </div>
    </div>
  </div>
  <div v-else class="text-center mt-10">
    <p>You must be logged in to access goals.</p>
    <router-link to="/login" class="text-blue-500">Log In</router-link>
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

    // State to control form visibility and section toggles
    const showForm = ref(false);
    const showPersonalGoals = ref(true);
    const showGroupGoals = ref(true);
    const showCompletedGoals = ref(false);

    // Goal properties
    const title = ref('');
    const description = ref('');
    const hasDeadline = ref(false);
    const deadline = ref('');
    const successMessage = ref('');
    const errorMessage = ref('');
    const selectedGroup = ref('');
    const groups = ref([]);
    const goalType = ref('personal');
    const category = ref('');

    // User-specific data
    const userGroups = ref([]);
    const userId = ref(null);  // Fetch current user id

    // Goals data
    const goals = ref([]);

    // Fetch user's personal goals
    const personalGoals = computed(() => goals.value.filter(goal => !goal.is_group_goal && !goal.completed && goal.user_id === userId.value));

    // Fetch user's group goals (user must be part of the group)
    const groupGoals = computed(() => {
      return goals.value.filter(goal => {
        return goal.is_group_goal && !goal.completed && userGroups.value.some(group => group.id === goal.group_id);
      });
    });

    // Fetch completed goals (either the user's goals or goals from their groups)
    const completedGoals = computed(() => {
      return goals.value.filter(goal => {
        const isGroupGoal = goal.is_group_goal && userGroups.value.some(group => group.id === goal.group_id);
        const isPersonalGoal = !goal.is_group_goal && goal.user_id === userId.value;
        return goal.completed && (isGroupGoal || isPersonalGoal);
      });
    });

    onMounted(async () => {
      await fetchUserDetails();  // Fetch user details to get id and groups
      await fetchGoals();
      await fetchGroups();
    });

    // Fetch user details to get current user id and groups
    const fetchUserDetails = async () => {
      try {
        const response = await axios.get('/user'); // Assuming you have a /user endpoint
        userId.value = response.data.id;
        userGroups.value = response.data.groups;  // Get groups the user belongs to
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    };

    // Fetch goals
    const fetchGoals = async () => {
      try {
        const response = await axios.get('/goals');
        goals.value = response.data;
      } catch (error) {
        console.error('Error fetching goals:', error);
      }
    };

    // Fetch groups
    const fetchGroups = async () => {
      try {
        const response = await axios.get('/groups');
        groups.value = response.data;
      } catch (error) {
        console.error('Error fetching groups:', error);
      }
    };

    const addGoal = async () => {
      if (!title.value ) {
        errorMessage.value = 'Please provide a title and description for the goal.';
        return;
      }

      if (!category.value) {
        errorMessage.value = 'Please select a category.';
        return;     
      }

      errorMessage.value = '';

      const titleCapitalized = title.value
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

      const descriptionCapitalized = description.value
        ? `${description.value.charAt(0).toUpperCase()}${description.value.slice(1)}${/[\w]$/.test(description.value) && !/[.!?]$/.test(description.value) ? '.' : ''}`
        : '';

     const goalData = {
        title: titleCapitalized,
        description: descriptionCapitalized,
        hasDeadline: hasDeadline.value,
        deadline: hasDeadline.value ? deadline.value : null,
        is_group_goal: goalType.value === 'group',
        group_id: goalType.value === 'group' ? selectedGroup.value : null,
        category: category.value,
      };



      try {
        const response = await axios.post('/goals', goalData);
        goals.value.push(response.data);
        successMessage.value = 'Goal added successfully!';
        clearForm();
        await fetchGoals();
        setTimeout(() => successMessage.value = '', 4000);
      } catch (error) {
        errorMessage.value = 'Failed to add goal.';
        console.error("Error adding goal:", error);
        setTimeout(() => errorMessage.value = '', 4000);
      }
    };

    const clearForm = () => {
      title.value = '';
      description.value = '';
      hasDeadline.value = false;
      deadline.value = '';
      selectedGroup.value = '';
      goalType.value = 'personal';
      category.value = '';
    };

    const toggleGoalCompletion = async (goal) => {
      try {
        goal.completed = !goal.completed;
        await axios.put(`/goals/${goal.id}`, { completed: goal.completed });
      } catch (error) {
        console.error("Error toggling goal completion:", error);
      }
    };

    const deleteGoal = async (goalId) => {
      try {
        await axios.delete(`/goals/${goalId}`);
        goals.value = goals.value.filter(goal => goal.id !== goalId);
      } catch (error) {
        console.error("Error deleting goal:", error);
      }
    };

    return {
      title,
      description,
      hasDeadline,
      deadline,
      successMessage,
      errorMessage,
      selectedGroup,
      groups,
      goalType,
      category,
      personalGoals,
      groupGoals,
      completedGoals,
      isAuthenticated,
      showForm,
      showPersonalGoals,
      showGroupGoals,
      showCompletedGoals,
      addGoal,
      toggleGoalCompletion,
      deleteGoal,
    };
  },
};
</script>


<style scoped>
/* Add any specific styles you want for this component here */
.cursor-pointer {
  cursor: pointer;
}

.transition-transform {
  transition: transform 0.3s;
}
</style>
