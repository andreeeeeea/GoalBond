<template>
    <div class="group-list">
      <h2 class="text-2xl font-semibold mb-4">My Groups</h2>
      <ul v-if="groups.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <li v-for="group in groups" :key="group.id" class="bg-white rounded-lg shadow p-4">
          <h3 class="text-lg font-bold">{{ group.name }}</h3>
          <p class="text-gray-700">{{ group.description }}</p>
  
          <!-- Display members of the group -->
          <h4 class="font-semibold mt-2">Members:</h4>
          <ul v-if="group.members && group.members.length > 0">
            <span v-for="(member, index) in group.members" :key="member.id">
              {{ member.username }}{{ index === group.members.length - 1 ? '.' : ', ' }}
            </span>
          </ul>
          <p v-else class="text-gray-500">No members yet.</p>
  
          <button 
            @click="leaveGroup(group.id)" 
            class="mt-4 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500 transition duration-300"
          >
            Leave Group
          </button>
        </li>
      </ul>
      <p v-else class="text-center">No groups available yet.</p>
      
      <!-- Display success or error message -->
      <div v-if="successMessage" class="text-green-500 text-center mt-4">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="text-red-500 text-center mt-4">
        {{ errorMessage }}
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        groups: [],
        successMessage: '', // New property for success message
        errorMessage: '',   // New property for error message
      }
    },
    mounted() {
      this.fetchUserGroups(); // Fetch the user's groups when the component is mounted
    },
    methods: {
      fetchUserGroups() {
        axios.get('http://localhost:5000/groups/mine')
        .then(response => {
            this.groups = response.data; // Update the groups array with user's groups
        })
        .catch(error => {
            console.error('Error fetching groups:', error); // Log the error for debugging
        });
      },
      leaveGroup(groupId) {
        axios.post(`http://localhost:5000/groups/${groupId}/leave`)
          .then(response => {
            this.successMessage = response.data.message; // Set success message from response
            this.errorMessage = ''; // Clear any previous error message
            this.fetchUserGroups(); // Refresh the group list after leaving
          })
          .catch(error => {
            this.errorMessage = error.response.data.message || 'An error occurred while leaving the group.'; // Handle error message
            this.successMessage = ''; // Clear any previous success message
            console.error('Error leaving group:', error); // Log the error for debugging
          });
      }
    }
  }
  </script>
  
  <style scoped>
  .group-list {
    max-width: 500px;
    margin: 0 auto;
  }
  </style>
  