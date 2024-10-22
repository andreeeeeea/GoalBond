<template>
    <div class="flex flex-col items-center justify-center pt-14">
      <h2 class="text-2xl font-bold">Account</h2>
      <p>Username: {{ username }}</p>
      <p>Email: {{ email }}</p>
      <div class="py-6">
        <button
              v-if="isAuthenticated"
              @click="logout"
              class="text-white bg-red-600 hover:bg-red-700 px-4 py-2 rounded transition duration-300"
            >
              Logout
        </button>
      </div>
      <h3 class="text-xl font-semibold mt-4">Public Groups Joined:</h3>
      <ul v-if="publicGroups.length > 0" class="mt-2">
        <li v-for="group in publicGroups" :key="group.id" class="border-b py-2">
          {{ group.name }}: {{ group.description }}
        </li>
      </ul>
      <p v-else class="mt-2">No public groups joined yet.</p>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  import axios from 'axios';
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const store = useStore();
      const router = useRouter(); 

      const logout = async () => {
      await store.dispatch('logout');
      router.push('/login');
    };

    return {
      logout,
    };
    },

    computed: {
      ...mapGetters(['getUsername', 'getEmail', 'isAuthenticated']),
      username() {
        return this.getUsername; // Access username from Vuex
      },
      email() {
        return this.getEmail; // Access email from Vuex
      }
    },
    data() {
      return {
        publicGroups: [] // Store public groups
      };
    },
    mounted() {
      this.fetchPublicGroups(); // Fetch public groups on component mount
    },
    methods: {
      async fetchPublicGroups() {
        try {
          const response = await axios.get('/groups'); // Fetch public groups
          this.publicGroups = response.data.filter(group => 
            group.is_public && group.members.some(member => member.username === this.username)
          );
        } catch (error) {
          console.error('Error fetching public groups:', error); // Handle error fetching groups
        }
      },
      
    }
  };
  </script>
  
  <style scoped>
  /* Add any styles if needed */
  </style>
  