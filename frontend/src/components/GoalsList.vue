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
            class="bg-gray-800 text-white font-bold py-3 px-6 rounded-lg hover:bg-gray-500 transition duration-300"
          >
            {{ showForm ? 'Cancel' : 'Add Goal' }}
          </button>
        </div>
        <!-- Add Goal Section -->
        <div v-if="showForm" class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md mt-4">
          <h2 class="text-2xl font-semibold mb-4 text-center">Add Goal</h2>
          <form @submit.prevent="addGoal">
            <div class="mb-4 flex items-center justify-center">
              <label>
                <input type="radio" v-model="goalType" value="personal" /> Personal Goal
              </label>
              <div v-if="userGroups.length > 0" class="ml-4">
                <label class="ml-4">
                  <input type="radio" v-model="goalType" value="group" /> Group Goal
                </label>
              </div>
            </div>

            <!-- Show group selection only if the goal type is 'group' and the user has groups -->
            <div v-if="goalType === 'group' && userGroups.length > 0" class="mb-4">
              <select v-model="selectedGroup" class="w-full p-2 border border-gray-300 rounded-lg">
                <option disabled value="">Select a Group</option>
                <option v-for="group in userGroups" :key="group.id" :value="group.id">{{ group.name }}</option>
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
        
        <!-- Navigation for Goal Types -->
        <div class="flex space-x-4 mb-4">
          <span 
            @click="showPersonalGoals = true; showGroupGoals = false; showCompletedGoals = false"
            :class="['cursor-pointer', showPersonalGoals ? 'font-bold text-gray-700' : 'text-gray-600']"
          >
            Personal Goals
          </span>
          <span 
            @click="showPersonalGoals = false; showGroupGoals = true; showCompletedGoals = false"
            :class="['cursor-pointer', showGroupGoals ? 'font-bold text-gray-700' : 'text-gray-600']"
          >
            Group Goals
          </span>
          <span 
            @click="showPersonalGoals = false; showGroupGoals = false; showCompletedGoals = true"
            :class="['cursor-pointer', showCompletedGoals ? 'font-bold text-gray-700' : 'text-gray-600']"
          >
            Completed Goals
          </span>
        </div>

        <!-- Display Goals Based on the Selected Type -->
        <div v-if="showPersonalGoals" class="py-4">
          <div v-if="personalGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in personalGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <div class="flex-grow flex flex-col items-center">
                <div class="block text-xl text-gray-700 my-4"><strong>{{ goal.title }}</strong></div>
                <div class="block text-lg text-gray-700">{{  goal.description }}</div>
                <div class="block text-lg text-gray-700" v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</div>
                <span v-if="goal.deadline">
                  <span v-if="(new Date(goal.deadline) - new Date()) > 86400000">
                    <div div class="block text-lg text-gray-700">{{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60 * 24)) }} days left </div>
                  </span>
                  <span v-else-if="(new Date(goal.deadline) - new Date()) > 0">
                    <div class="block text-lg text-red-500"> {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60)) }} hours left </div>
                  </span>
                  <span v-else class="flex flex-col items-center justify-center">
                    Deadline passed
                    <div class="block text-lg text-gray-700">{{ new Date(goal.deadline).toLocaleDateString() }}</div>
                  </span>
                </span>
              </div>
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
                  <button @click="goalToUpdate = null" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Cancel
                  </button>
                </div>
              </div>
              <div class="relative inline-block text-left">
                <button
                  @click="toggleDropdown(goal.id)"
                  class="inline-flex justify-center w-28 rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Options
                  <svg
                    class="-mr-1 ml-2 h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>

                <div
                  v-bind:class="{'visible': openGoalId === goal.id, 'hidden': openGoalId !== goal.id}"
                  class="origin-top-right absolute left-0 w-36 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                >
                  <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="actions-menu">
                    <div class="flex items-center justify-left ml-2 mb-2">
                      <button
                        class="text-gray-600 hover:bg-gray-100 font-bold rounded w-auto text-sm block w-full"
                        @click="toggleGoalCompletion(goal)"
                      >
                        Mark as Completed
                      </button>
                    </div>
                    <div class="flex items-center justify-left ml-2">
                      <button
                        class="text-gray-600 hover:text-black font-bold rounded w-auto text-sm block w-full"
                        @click="deleteGoal(goal.id)"
                      >
                        Delete Goal
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No personal goals found in this category.</p>
          </div>
        </div>

        <!-- Display Group Goals -->
        <div v-if="showGroupGoals" class="py-4">
          <div v-if="groupGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in groupGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <div class="flex-grow flex flex-col items-center">
                <div class="block text-xl text-gray-700 my-4"><strong>{{ goal.title }}</strong></div>
                <div class="block text-lg text-gray-700">{{  goal.description }}</div>
                <div class="block text-lg text-gray-700" v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</div>
                <div class="block text-lg text-gray-700">Group: {{ goal.group.name }}</div>
                <span v-if="goal.deadline">
                  <span v-if="(new Date(goal.deadline) - new Date()) > 86400000">
                    <div div class="block text-lg text-gray-700">{{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60 * 24)) }} days left </div>
                  </span>
                  <span v-else-if="(new Date(goal.deadline) - new Date()) > 0">
                    <div class="block text-lg text-red-500"> {{ Math.floor((new Date(goal.deadline) - new Date()) / (1000 * 60 * 60)) }} hours left </div>
                  </span>
                  <span v-else class="flex flex-col items-center justify-center">
                    Deadline passed
                    <div class="block text-lg text-gray-700">{{ new Date(goal.deadline).toLocaleDateString() }}</div>
                  </span>
                </span>
              </div>
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
                  <button @click="goalToUpdate = null" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                    Cancel
                  </button>
                </div>
              </div>
              <div class="relative inline-block text-left">
                <button
                  @click="toggleDropdown(goal.id)"
                  class="inline-flex justify-center w-28 rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Options
                  <svg
                    class="-mr-1 ml-2 h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>

                <div
                  v-bind:class="{'visible': openGoalId === goal.id, 'hidden': openGoalId !== goal.id}"
                  class="origin-top-right absolute left-0 w-36 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                >
                  <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="actions-menu">
                    <div class="flex items-center justify-left ml-2 mb-2">
                      <button
                        class="text-gray-600 hover:bg-gray-100 font-bold rounded w-auto text-sm block w-full"
                        @click="toggleGoalCompletion(goal)"
                      >
                        Mark as Completed
                      </button>
                    </div>
                    <div class="flex items-center justify-left ml-2">
                      <button
                        class="text-gray-600 hover:text-black font-bold rounded w-auto text-sm block w-full"
                        @click="deleteGoal(goal.id)"
                      >
                        Delete Goal
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-else class="text-center mt-4">
            <p>No group goals found in this category.</p>
          </div>
        </div>

        <!-- Display Completed Goals -->
        <div v-if="showCompletedGoals" class="py-4">
          <div v-if="completedGoalsByCategory.length > 0" class="grid grid-cols-4 gap-4">
            <div v-for="goal in completedGoalsByCategory" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-80">
              <div class="flex-grow flex flex-col items-center">
                <div class="block text-xl text-gray-700 my-4"><strong>{{ goal.title }}</strong></div>
                <div class="block text-lg text-gray-700">{{  goal.description }}</div>
                <div class="block text-lg text-gray-700" v-if="goal.season && goal.episode">Season: {{ goal.season }} Episode: {{ goal.episode }}</div>
                <div class="block text-lg text-gray-700" v-if="goal.deadline">{{ new Date(goal.deadline).toLocaleDateString() }}</div>
              </div>

              <div class="relative inline-block text-left">
                <button
                  @click="toggleDropdown(goal.id)"
                  class="inline-flex justify-center w-28 rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Options
                  <svg
                    class="-mr-1 ml-2 h-5 w-5"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    aria-hidden="true"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>

                <div
                  v-bind:class="{'visible': openGoalId === goal.id, 'hidden': openGoalId !== goal.id}"
                  class="origin-top-right absolute left-0 w-36 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
                >
                  <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="actions-menu">
                    <div class="flex items-center justify-left ml-2 mb-2">
                      <button 
                        class="text-gray-600 hover:text-black font-bold rounded w-auto text-sm block w-full"
                        @click="redoGoal(goal)"
                        >
                        Re-Do Goal
                      </button>
                    </div>
                    <div class="flex items-center justify-left ml-2">
                      <button
                        class="text-gray-600 hover:text-black font-bold rounded w-auto text-sm block w-full"
                        @click="deleteGoal(goal.id)"
                      >
                        Delete Goal
                      </button>
                    </div>
                  </div>
                </div>
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
  props: {
    goal: {
      type: Object,
      required: true,
    },
  },

  // Component-specific reactive data
  data() {
    return {
      dropdowns: ref({}),
      openGoalId: null,
      successMessage: '',
      errorMessage: '',
      selectedGroup: '',
      showForm: false,
      showPersonalGoals: true,
      showGroupGoals: false,
      showCompletedGoals: false,
    };
  },

  // Methods
  methods: {
    toggleDropdown(goalId) {
      this.openGoalId = this.openGoalId === goalId ? null : goalId;
    },

    redoGoal(goal) {
      const newGoal = {
        title: goal.title,
        description: goal.description,
        hasDeadline: goal.hasDeadline,
        deadline: goal.deadline,
        is_group_goal: goal.is_group_goal,
        group_id: goal.group_id,
        category: goal.category,
        season: goal.season,
        episode: goal.episode,
      };
      axios.post('/goals', newGoal)
        .then(response => {
          this.goals.push(response.data);
          this.fetchGoals(); // Ensure this method is in your methods or setup.
        })
        .catch(error => {
          console.error("Error redoing goal:", error);
        });
    },

    // Goal completion toggle
    async toggleGoalCompletion(goal) {
      try {
        goal.completed = !goal.completed;
        await axios.put(`/goals/${goal.id}`, { completed: goal.completed });
      } catch (error) {
        console.error('Error toggling goal completion:', error);
      }
    },

    // Delete goal
    async deleteGoal(goalId) {
      try {
        await axios.delete(`/goals/${goalId}`);
        this.goals = this.goals.filter((goal) => goal.id !== goalId);
      } catch (error) {
        console.error('Error deleting goal:', error);
      }
    },

    // Show goal update form
    showUpdateForm(goal) {
      console.log('Showing update form for goal:', goal);
      this.goalToUpdate = { ...goal };
    },

    // Cancel goal update
    cancelUpdate() {
      this.goalToUpdate = null;
    },

    // Select a goal category
    selectCategory(category) {
      this.selectedCategory = category;
    },
  },

  setup() {
    const store = useStore();
    // eslint-disable-next-line no-unused-vars
    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    console.log('isAuthenticated:', isAuthenticated.value);

    // Reactive properties for goals and user details
    const title = ref('');
    const description = ref('');
    const hasDeadline = ref(false);
    const deadline = ref('');
    const category = ref('');
    const season = ref('');
    const episode = ref('');
    const goalToUpdate = ref(null);

    // User and group data
    const userId = ref(null);
    const userGroups = ref([]);
    const groups = ref([]);

    // Goals data
    const goals = ref([]);

    // Available categories
    const goalCategories = [
      'Books',
      'Coding',
      'Cooking',
      'Fitness',
      'Food and Dining',
      'Movies',
      'Series',
      'Music',
      'Photography',
      'Travel',
      'Other',
    ];

    // Selected category
    const selectedCategory = ref(goalCategories[0]);

    // Computed properties
    const personalGoalsByCategory = computed(() =>
      goals.value.filter(
        (goal) =>
          !goal.is_group_goal &&
          goal.category === selectedCategory.value &&
          !goal.completed &&
          goal.user_id === userId.value
      )
    );

    const groupGoalsByCategory = computed(() =>
      goals.value.filter(
        (goal) =>
          goal.is_group_goal &&
          goal.category === selectedCategory.value &&
          !goal.completed &&
          userGroups.value.some((group) => group.id === goal.group_id)
      )
    );

    const completedGoalsByCategory = computed(() =>
      goals.value.filter(
        (goal) =>
          goal.category === selectedCategory.value &&
          goal.completed &&
          (userGroups.value.some((group) => group.id === goal.group_id) ||
            goal.user_id === userId.value)
      )
    );

    // Fetch user details
    const fetchUserDetails = async () => {
      try {
        const response = await axios.get('/user');
        userId.value = response.data.id;
        userGroups.value = response.data.groups;
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    };

    // Fetch all goals
    const fetchGoals = async () => {
      try {
        const response = await axios.get('/goals');
        goals.value = response.data;
      } catch (error) {
        console.error('Error fetching goals:', error);
      }
    };

    // Fetch user groups
    const fetchGroups = async () => {
      try {
        const response = await axios.get('/groups');
        groups.value = response.data;
      } catch (error) {
        console.error('Error fetching groups:', error);
      }
    };

    // Add a new goal
    const addGoal = async () => {
      if (!title.value) {
        console.error('Title is required.');
        return;
      }

      const newGoal = {
        title: title.value,
        description: description.value,
        hasDeadline: hasDeadline.value,
        deadline: hasDeadline.value ? deadline.value : null,
        category: category.value,
        season: category.value === 'Series' ? season.value : null,
        episode: category.value === 'Series' ? episode.value : null,
      };

      try {
        const response = await axios.post('/goals', newGoal);
        goals.value.push(response.data);
      } catch (error) {
        console.error('Failed to add goal:', error);
      }
    };

    onMounted(async () => {
      await fetchUserDetails();
      await fetchGoals();
      await fetchGroups();
    });

    return {
      isAuthenticated,
      title,
      description,
      hasDeadline,
      deadline,
      category,
      season,
      episode,
      goalToUpdate,
      goals,
      groups,
      userId,
      userGroups,
      goalCategories,
      selectedCategory,
      personalGoalsByCategory,
      groupGoalsByCategory,
      completedGoalsByCategory,
      fetchGoals,
      fetchUserDetails,
      addGoal,
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