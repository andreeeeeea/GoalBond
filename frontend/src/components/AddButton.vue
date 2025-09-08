<template>
  <div v-if="isAuthenticated">
    <div class="group fixed bottom-3 right-4">
      <div class="absolute -inset-20 bg-transparent"></div>
      
      <div class="relative p-3 flex items-end justify-end">
        <div class="text-white shadow-2xl flex items-center justify-center p-4 rounded-full h-16 w-16 bg-[#B03052] z-50">
          <span class="flex items-center justify-center text-3xl">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none">
              <path d="M6 12H18M12 6V18" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </span>
        </div>
    
        <!-- Add Group Button -->
        <div class="absolute rounded-full transition-all duration-200 ease-out scale-y-0 group-hover:scale-y-100 group-hover:-translate-x-20 flex items-center justify-center p-4 hover:p-4 bg-[#B03052] hover:bg-[#3D0301] text-white h-16 w-16" @click="showGroupForm = true">
          <span class="flex items-center justify-center w-full h-full text-3xl">
            <svg xmlns="http://www.w3.org/2000/svg" width="800px" height="800px" viewBox="0 0 24 24" fill="none">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M16 6C14.3432 6 13 7.34315 13 9C13 10.6569 14.3432 12 16 12C17.6569 12 19 10.6569 19 9C19 7.34315 17.6569 6 16 6ZM11 9C11 6.23858 13.2386 4 16 4C18.7614 4 21 6.23858 21 9C21 10.3193 20.489 11.5193 19.6542 12.4128C21.4951 13.0124 22.9176 14.1993 23.8264 15.5329C24.1374 15.9893 24.0195 16.6114 23.5631 16.9224C23.1068 17.2334 22.4846 17.1155 22.1736 16.6591C21.1979 15.2273 19.4178 14 17 14C13.166 14 11 17.0742 11 19C11 19.5523 10.5523 20 10 20C9.44773 20 9.00001 19.5523 9.00001 19C9.00001 18.308 9.15848 17.57 9.46082 16.8425C9.38379 16.7931 9.3123 16.7323 9.24889 16.6602C8.42804 15.7262 7.15417 15 5.50001 15C3.84585 15 2.57199 15.7262 1.75114 16.6602C1.38655 17.075 0.754692 17.1157 0.339855 16.7511C-0.0749807 16.3865 -0.115709 15.7547 0.248886 15.3398C0.809035 14.7025 1.51784 14.1364 2.35725 13.7207C1.51989 12.9035 1.00001 11.7625 1.00001 10.5C1.00001 8.01472 3.01473 6 5.50001 6C7.98529 6 10 8.01472 10 10.5C10 11.7625 9.48013 12.9035 8.64278 13.7207C9.36518 14.0785 9.99085 14.5476 10.5083 15.0777C11.152 14.2659 11.9886 13.5382 12.9922 12.9945C11.7822 12.0819 11 10.6323 11 9ZM3.00001 10.5C3.00001 9.11929 4.1193 8 5.50001 8C6.88072 8 8.00001 9.11929 8.00001 10.5C8.00001 11.8807 6.88072 13 5.50001 13C4.1193 13 3.00001 11.8807 3.00001 10.5Z" fill="white"/>
            </svg>
          </span>
        </div>

        <!-- Add Goal Button -->
        <div class="absolute rounded-full transition-all duration-200 ease-out scale-x-0 group-hover:scale-x-100 group-hover:-translate-y-20 flex items-center justify-center p-4 hover:p-4 bg-[#B03052] hover:bg-[#3D0301] text-white h-16 w-16" @click="showForm = true">
          <span class="flex items-center justify-center w-full h-full text-3xl">
            <svg xmlns="http://www.w3.org/2000/svg" width="800px" height="800px" viewBox="0 0 16 16" fill="none">
                <path d="M8.16923 2.00234C8.11301 2.00078 8.0566 2 8 2C4.68629 2 2 4.68629 2 8C2 11.3137 4.68629 14 8 14C11.3137 14 14 11.3137 14 8C14 7.9434 13.9992 7.88699 13.9977 7.83077L15.7642 6.06422C15.9182 6.68407 16 7.33249 16 8C16 12.4183 12.4183 16 8 16C3.58172 16 0 12.4183 0 8C0 3.58172 3.58172 0 8 0C8.66751 0 9.31593 0.0817526 9.93578 0.235791L8.16923 2.00234Z" fill="#FFFFFF"/>
                <path d="M4 7.99996C4 6.13612 5.27477 4.57002 7 4.12598V6.26752C6.4022 6.61333 6 7.25968 6 7.99996C6 9.10453 6.89543 9.99996 8 9.99996C8.74028 9.99996 9.38663 9.59776 9.73244 8.99996H11.874C11.4299 10.7252 9.86384 12 8 12C5.79086 12 4 10.2091 4 7.99996Z" fill="#FFFFFF"/>
                <path d="M14 2L13 0L10 3V4.58579L7.79289 6.79289L9.20711 8.20711L11.4142 6H13L16 3L14 2Z" fill="#FFFFFF"/>
            </svg>
          </span>
        </div>
      </div>
    </div>
    <!-- Add Goal Form -->
    <div v-if="showForm" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75 backdrop-blur-sm z-[9999]">
      <div class="max-w-lg w-full p-6 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold mb-4 text-center">Create New Goal</h2>
        <form @submit.prevent="addGoal">
          <!-- Debug info - remove after testing -->
          <div v-if="false" class="mb-2 p-2 bg-gray-100 text-sm">
            Debug: goalType={{ goalType }}, userGroups.length={{ userGroups.length }}
          </div>
          
          <div class="mb-4 flex items-center justify-center">
            <div class="flex gap-4">
              <label class="inline-flex items-center cursor-pointer">
                <input 
                  type="radio" 
                  name="goalType" 
                  v-model="goalType" 
                  value="personal" 
                  class="form-radio text-[#D76C82] focus:ring-[#D76C82]" 
                />
                <span class="ml-2">Personal Goal</span>
              </label>
              <label v-if="userGroups && userGroups.length > 0" class="inline-flex items-center cursor-pointer">
                <input 
                  type="radio" 
                  name="goalType" 
                  v-model="goalType" 
                  value="group" 
                  class="form-radio text-[#D76C82] focus:ring-[#D76C82]" 
                />
                <span class="ml-2">Group Goal</span>
              </label>
            </div>
          </div>

          <div v-if="goalType === 'group' && userGroups.length > 0" class="mb-4">
            <select v-model="selectedGroup" class="w-full p-2 border border-gray-300 rounded-lg">
              <option disabled value="">Select a Group</option>
              <option v-for="group in userGroups" :key="group.id" :value="group.id">{{ group.name }}</option>
            </select>
          </div>

          <div class="mb-4">
            <input v-model="title" type="text" placeholder="Goal Title" class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#D76C82]" />
          </div>

          <div class="mb-4">
            <textarea v-model="description" placeholder="Description" class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#D76C82]"></textarea>
          </div>

          <div class="mb-4">
            <label for="category">Category:</label>
            <select v-model="category" id="category" class="w-full p-2 border border-gray-300 rounded-lg">
              <option disabled value="">Select a Category</option>
              <option v-for="category in goalCategories" :key="category" :value="category">{{ category }}</option>
            </select>
          </div>

          <div v-if="category === 'Series'" class="mb-4">
            <label for="season">Season:</label>
            <input type="number" id="season" v-model="season" class="w-full p-2 border border-gray-300 rounded-lg" />
          </div>

          <div v-if="category === 'Series'" class="mb-4">
            <label for="episode">Episode:</label>
            <input type="number" id="episode" v-model="episode" class="w-full p-2 border border-gray-300 rounded-lg" />
          </div>

          <div class="mb-4">
            <input type="checkbox" id="hasDeadline" v-model="hasDeadline" />
            <label for="hasDeadline"> Add Deadline?</label>
          </div>

          <div v-if="hasDeadline" class="mb-4">
            <label for="deadline">Deadline:</label>
            <input type="date" id="deadline" v-model="deadline" required />
          </div>

          <div class="flex justify-between space-x-2">
            <button type="submit" class="bg-[#D76C82] hover:bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg transition duration-300">Add Goal</button>
            <button @click="showForm = false" type="button" class="border-4 border-[#D76C82] text-[#D76C82] font-bold py-2 px-4 rounded-lg hover:bg-[#B03052] hover:border-[#B03052] hover:text-white transition duration-300">Cancel</button>
          </div>
        </form>
      </div>
    </div>

    <div v-if="showGroupForm" class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75 backdrop-blur-sm z-[9999]">
      <div class="max-w-lg w-full p-6 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold mb-4 text-center">Create New Group</h2>
        <form @submit.prevent="createGroup">
          <div class="mb-4">
            <input
              v-model="name"
              type="text"
              placeholder="Group Name"
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#D76C82]"
              required
            />
          </div>

          <div class="mb-4">
            <textarea
              v-model="groupDescription"
              placeholder="Group Description"
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#D76C82] resize-none h-32"
            ></textarea>
          </div>

          <div class="mb-4">
            <label class="block mb-2">Group Privacy:</label>
            <select 
              v-model="isPublic" 
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#D76C82]"
            >
              <option :value="true">Public</option>
              <option :value="false">Private</option>
            </select>
          </div>

          <div class="flex justify-between space-x-2">
            <button type="submit" class="bg-[#D76C82] hover:bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg transition duration-300"> Create Group </button>
            <button @click="showGroupForm = false" type="button" class="border-4 border-[#D76C82] text-[#D76C82] font-bold py-2 px-4 rounded-lg hover:bg-[#B03052] hover:border-[#B03052] hover:text-white transition duration-300"> Cancel </button>
          </div>
        </form>
      </div>
    </div>
  </div>

</template>
  
<script>
import { useStore } from 'vuex';
import { useToast } from "vue-toastification";
import axios from 'axios';
import { eventBus } from '@/eventBus';

export default {
  setup() {
    const store = useStore();
    return { store };
  },
  data() {
    return {
      showButtons: false,
      showForm: false,
      showGroupForm: false,
      title: '',
      description: '',
      hasDeadline: false,
      deadline: '',
      goalType: 'personal',
      selectedGroup: '',
      category: '',
      season: '',
      episode: '',
      userGroups: [],
      goalCategories: [
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
      ],
      name: '',
      groupDescription: '',
      isPublic: true,
    };
  },
  methods: {
    toggleButtons() {
      this.showForm = !this.showForm;
      // Fetch user groups when opening the form
      if (this.showForm) {
        this.fetchUserGroups();
      }
    },
    async addGoal() {
      if (!this.title) {
        this.toast.error('Title is required.');
        return;
      }

      if (!this.category) {
        this.toast.error('Category is required.');
        return;
      }

      if (this.category === 'Series' && (!this.season || !this.episode)) {
        this.toast.error('Season and Episode are required.');
        return;
      }

      const titleCapitalized = this.title
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');

      const descriptionCapitalized = this.description
        ? `${this.description.charAt(0).toUpperCase()}${this.description.slice(1)}${/[\w]$/.test(this.description) && !/[.!?]$/.test(this.description) ? '.' : ''}`
        : '';

      const goalData = {
        title: titleCapitalized,
        description: descriptionCapitalized,
        hasDeadline: this.hasDeadline,
        deadline: this.hasDeadline ? this.deadline : null,
        is_group_goal: this.goalType === 'group',
        group_id: this.goalType === 'group' ? this.selectedGroup : null,
        category: this.category,
        season: this.category === 'Series' ? this.season : null,
        episode: this.category === 'Series' ? this.episode : null,
      };

      try {
        const response = await axios.post('/goals', goalData);
        this.clearForm();
        this.showForm = false;
        this.toast.success('Goal added successfully.');
        this.$emit('goal-added', response.data);
        // Emit event to refresh goals list
        eventBus.emit('goal-added', response.data);
      } catch (error) {
        console.error("Error adding goal:", error);
        this.toast.error('Goal could not be added. Please try again.');
      }
    },
    clearForm() {
      this.title = '';
      this.description = '';
      this.hasDeadline = false;
      this.deadline = '';
      this.selectedGroup = '';
      this.goalType = 'personal';
      this.category = '';
      this.season = '';
      this.episode = '';
    },
    clearGroupForm() {
      this.name = '';
      this.groupDescription = '';
      this.isPublic = true;
    },
    async fetchUserGroups() {
      try {
        const response = await axios.get('/user');
        console.log('User data response:', response.data);
        this.userGroups = response.data.groups || [];
        console.log('User groups loaded:', this.userGroups);
        
        // If user has no groups, show a message
        if (this.userGroups.length === 0) {
          console.log('User has no groups');
        }
      } catch (error) {
        console.error('Error fetching user groups:', error);
        if (error.response?.status === 401) {
          this.userGroups = [];
          console.log('User not authenticated');
        } else {
          this.userGroups = [];
          this.toast.error('Failed to load groups. Please try again.');
        }
      }
    },
    async createGroup() {
      if(!this.name) {
        this.toast.error('Group name is required.');
        return;
      }

      try {
        await axios.post('/groups', {
          name: this.name,
          description: this.groupDescription,
          is_public: this.isPublic,
        });
        this.toast.success('Group created successfully!');
        this.clearGroupForm();
        this.showGroupForm = false;
        await this.fetchUserGroups();
        // Emit event to refresh groups list
        eventBus.emit('group-added');
      } catch (error) {
        console.error('Error creating group:', error);
        this.toast.error('An error occurred while creating the group.');
      }
    }
  },
  async mounted() {
    this.toast = useToast();
    await this.fetchUserGroups();
  },
  watch: {
    goalType(newVal) {
      console.log('Goal type changed to:', newVal);
    },
    selectedGroup(newVal) {
      console.log('Selected group changed to:', newVal);
    }
  },
  computed: {
    isAuthenticated() {
      if (!this.store) return false;
      return this.store.getters.isAuthenticated;
    },
  },
};
</script>
  
<style scoped>
  /* Optional: Add any additional custom styles */
</style>
  


