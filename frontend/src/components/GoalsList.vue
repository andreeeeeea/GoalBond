<template>
  <div v-if="isAuthenticated" class="mx-4">   
    <section class="flex">
      <!-- Sidebar for Goal Categories -->
      <div class="w-1/6 bg-gray-100 py-4 h-screen overflow-y-auto">
        <h2 class="text-xl font-semibold mb-2">Goal Categories</h2>
        <div v-for="category in goalCategories" :key="category" @click="selectCategory(category)" :class="{ 'bg-gray-300': category === selectedCategory }" class="cursor-pointer p-2 mr-5 hover:bg-gray-300 rounded border-b">
          {{ category }}
        </div>
        <!-- Button to Toggle Form Visibility -->
        <div class="text-left mt-5">
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
                <option value="Series">Series</option>
                <option value="Music">Music</option>
                <option value="Photography">Photography</option>
                <option value="Travel">Travel</option>
                <option value="Other">Other</option>
              </select>
            </div>

            <div v-if="category === 'Series'" class="mb-4">
              <label for="season">Season:</label>
              <input type="number" id="season" v-model="season" class="w-full p-2 border border-gray-300 rounded-lg" required />
            </div>

            <div v-if="category === 'Series'" class="mb-4">
              <label for="episode">Episode:</label>
              <input type="number" id="episode" v-model="episode" class="w-full p-2 border border-gray-300 rounded-lg" required />
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
      </div>
      <div class=" min-h-[1em] w-px self-stretch bg-gradient-to-tr from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400"></div>
      <!-- Main section for displaying goals -->
      <div class="w-3/4 py-4 mx-10">
        <h2 class="text-3xl font-bold mb-4">{{ selectedCategory }}</h2>       
        <!-- Display Personal Goals -->
         <div class="py-4">
          <h3 class="text-lg font-semibold mb-2">Personal Goals</h3>
          <div v-if="personalGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in personalGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <!-- Goal Content -->
              <div class="flex-grow">
                <p class="text-lg font-semibold">{{ goal.title }}</p>
                <p>{{ goal.description }}</p>
                <p>Category: {{ goal.category }}</p>
                <p v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</p>
                <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
                <p>Status: {{ goal.completed ? 'Completed' : 'Not Completed' }}</p>
              </div>
              <!-- Goal Actions -->
              <div class="mb-2">
                <div v-if="goalToUpdate && goalToUpdate.id === goal.id">
                  <h4 class="mt-4 text-lg font-semibold">Update Current Episode</h4>
                  <div>
                    <label for="currentSeason">Season:</label>
                    <input type="number" id="currentSeason" v-model="goalToUpdate.season" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <div>
                    <label for="currentEpisode">Episode:</label>
                    <input type="number" id="currentEpisode" v-model="goalToUpdate.episode" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <button @click="updateGoal(goalToUpdate)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Save
                  </button>
                  <button @click="cancelUpdate" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Cancel
                  </button>
                </div>
              </div>
              <div v-if="!goalToUpdate || goalToUpdate.id !== goal.id" class="mt-auto justify-center">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
                <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
                <button v-if="goal.category === 'Series'" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="showUpdateForm(goal)">Update Goal</button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No personal goals found in this category.</p>
          </div>
         </div>
        <!-- Display Group Goals -->
         <div class="py-4">
          <h3 class="text-lg font-semibold mb-2">Group Goals</h3>
          <div v-if="groupGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in groupGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <!-- Goal Content -->
              <div class="flex-grow">
                <p class="text-lg font-semibold">{{ goal.title }}</p>
                <p>{{ goal.description }}</p>
                <p>Category: {{ goal.category }}</p>
                <p v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</p>
                <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
                <p>Status: {{ goal.completed ? 'Completed' : 'Not Completed' }}</p>
              </div>
              <!-- Goal Actions -->
              <div class="mb-2">
                <div v-if="goalToUpdate && goalToUpdate.id === goal.id">
                  <h4 class="mt-4 text-lg font-semibold">Update Current Episode</h4>
                  <div>
                    <label for="currentSeason">Season:</label>
                    <input type="number" id="currentSeason" v-model="goalToUpdate.season" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <div>
                    <label for="currentEpisode">Episode:</label>
                    <input type="number" id="currentEpisode" v-model="goalToUpdate.episode" min="1" class="border rounded py-1 px-2" required />
                  </div>
                  <button @click="updateGoal(goalToUpdate)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Save
                  </button>
                  <button @click="cancelUpdate" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Cancel
                  </button>
                </div>
              </div>
              <div v-if="!goalToUpdate || goalToUpdate.id !== goal.id" class="mt-auto justify-center">
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
                <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
                <button v-if="goal.category === 'Series'" class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="showUpdateForm(goal)">Update Goal</button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No group goals found in this category.</p>
          </div>
         </div>
        <!-- Display Completed Goals -->
         <div class="py-4">
          <h3 class="text-lg font-semibold mb-2">Completed Goals</h3>
          <div v-if="completedGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in completedGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <!-- Goal Content -->
              <div class="flex-grow">
                <p class="text-lg font-semibold">{{ goal.title }}</p>
                <p>{{ goal.description }}</p>
                <p>Category: {{ goal.category }}</p>
                <p v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</p>
                <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleDateString() }}</span>
                <p>Status: Completed</p>
              </div>
              <!-- Goal Actions -->
              <div v-if="!goalToUpdate || goalToUpdate.id !== goal.id" class="mt-auto justify-center">
                <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No completed goals found in this category.</p>
          </div>
         </div>
      </div>

    </section>
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
    const season = ref('');
    const episode = ref('');
    const goalToUpdate = ref(null); // New state for the goal to update

    // User-specific data
    const userGroups = ref([]);
    const userId = ref(null);  // Fetch current user id

    // Goals data
    const goals = ref([]);

    // Available goal categories
    const goalCategories = [
      'Books', 'Coding', 'Cooking', 'Fitness',
      'Food and Dining', 'Movies', 'Series',
      'Music', 'Photography', 'Travel', 'Other'
    ];

    const goalTypes = [
      'Personal', 'Group', 'Completed'
    ];

    // Selected category state
    const selectedCategory = ref(goalCategories[0]); // Default to the first category

    // Fetch user's personal goals
    const personalGoalsByCategory = computed(() => 
      goals.value.filter(goal => 
        !goal.is_group_goal && 
        goal.category === selectedCategory.value && 
        !goal.completed && 
        goal.user_id === userId.value
      )
    );

    // Fetch user's group goals (user must be part of the group)
    const groupGoalsByCategory = computed(() => 
      goals.value.filter(goal => 
        goal.is_group_goal && 
        goal.category === selectedCategory.value && 
        !goal.completed && 
        userGroups.value.some(group => group.id === goal.group_id)
      )
    );

    // Fetch completed goals (either the user's goals or goals from their groups)
    const completedGoalsByCategory = computed(() => 
      goals.value.filter(goal => 
        goal.category === selectedCategory.value && 
        goal.completed && 
        (userGroups.value.some(group => group.id === goal.group_id) || goal.user_id === userId.value)
      )
    );

    // Computed property to filter goals based on selected category
    const filteredGoals = computed(() => {
      return goals.value.filter(goal => goal.category === selectedCategory.value);
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

      if(category.value === 'Series' && (!season.value || !episode.value)) {
        errorMessage.value = 'Please provide a season and episode number.';
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
        season: category.value === 'Series' ? season.value : null,
        episode: category.value === 'Series' ? episode.value : null,
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
      season.value = '';
      episode.value = '';
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

    const updateGoal = async (goal) => {
      try {
        // Update the goal in the backend
        await axios.put(`/goals/${goal.id}`, {
          season: goal.season,
          episode: goal.episode,
        });
        
        // Refresh the goals after update
        await fetchGoals();

        // Clear the goal to update
        goalToUpdate.value = null;
      } catch (error) {
        console.error("Error updating goal:", error);
      }
    };

    const showUpdateForm = (goal) => {
      console.log('Showing update form for goal:', goal); // Log the goal
      goalToUpdate.value = { ...goal }; // Clone the goal to prevent direct mutation
    };

    const cancelUpdate = () => {
      goalToUpdate.value = null; // Reset the update state
    };

    // Method to select a category
    const selectCategory = (category) => {
      selectedCategory.value = category; // Update the selected category
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
      season,
      episode,
      goalToUpdate,
      personalGoalsByCategory,
      groupGoalsByCategory,
      completedGoalsByCategory,
      isAuthenticated,
      showForm,
      showPersonalGoals,
      showGroupGoals,
      showCompletedGoals,
      addGoal,
      toggleGoalCompletion,
      deleteGoal,
      updateGoal,
      showUpdateForm,
      cancelUpdate,
      goalCategories,
      goalTypes,
      selectedCategory,
      filteredGoals,
      selectCategory, // Expose the selectCategory method
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
