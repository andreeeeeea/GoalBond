<template>
    <div class="group-list">
      <h2 class="text-2xl font-semibold mb-4">Groups</h2>
      <ul v-if="groups.length > 0">
        <li v-for="group in groups" :key="group.id" class="mb-4 p-4 border border-gray-300 rounded-lg">
          <h3 class="text-lg font-bold">{{ group.name }}</h3>
          <p>{{ group.description }}</p>
  
          <!-- Display members of the group -->
          <h4 class="font-semibold mt-2">Members:</h4>
          <ul v-if="group.members && group.members.length > 0">
            <li v-for="member in group.members" :key="member.id">
              {{ member.username }} <!-- Assuming member has a username -->
            </li>
          </ul>
          <p v-else>No members yet.</p>
  
          <button @click="joinGroup(group.id)" class="mt-2 bg-green-600 text-white py-1 px-4 rounded hover:bg-green-500 transition duration-300">
            Join
          </button>
          <button @click="leaveGroup(group.id)" class="mt-2 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500 transition duration-300">
            Leave Group
          </button>
        </li>
      </ul>
      <p v-else>No groups available yet.</p>
      
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
      this.fetchGroups(); // Call a method to fetch groups
    },
    methods: {
      fetchGroups() {
        axios.get('http://localhost:5000/groups')
          .then(response => {
            this.groups = response.data; // Update the groups array
          })
          .catch(error => {
            console.error('Error fetching groups:', error); // Log the error for debugging
          });
      },
      joinGroup(groupId) {
        axios.post(`http://localhost:5000/groups/${groupId}/join`)
          .then(response => {
            this.successMessage = response.data.message; // Set success message from response
            this.errorMessage = ''; // Clear any previous error message
            this.fetchGroups(); // Refresh the group list after joining
          })
          .catch(error => {
            this.errorMessage = error.response.data.message || 'An error occurred while joining the group.'; // Handle error message
            this.successMessage = ''; // Clear any previous success message
            console.error('Error joining group:', error); // Log the error for debugging
          });
      },
      leaveGroup(groupId) {
        axios.post(`http://localhost:5000/groups/${groupId}/leave`)
          .then(response => {
            this.successMessage = response.data.message; // Set success message from response
            this.errorMessage = ''; // Clear any previous error message
            this.fetchGroups(); // Refresh the group list after leaving
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
  