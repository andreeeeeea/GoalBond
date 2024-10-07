<template>
    <div class="max-w-md mx-auto p-6 bg-white rounded-lg shadow-md mt-10">
      <h2 class="text-2xl font-semibold mb-4 text-center">Create Group</h2>
      <form @submit.prevent="createGroup" class="space-y-4">
        <div>
          <input 
            v-model="name" 
            type="text" 
            placeholder="Group Name" 
            class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
        <div>
          <textarea 
            v-model="description" 
            placeholder="Group Description" 
            class="border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          ></textarea>
        </div>
        <button 
          type="submit"
          class="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-500 transition duration-200"
        >
          Create Group
        </button>
        <div v-if="successMessage" class="text-green-500 text-center mt-2">{{ successMessage }}</div>
        <div v-if="errorMessage" class="text-red-500 text-center mt-2">{{ errorMessage }}</div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        name: '',
        description: '',
        successMessage: '',
        errorMessage: ''
      }
    },
    methods: {
      createGroup() {
        axios.post('/groups', {
          name: this.name,
          description: this.description
        })
        .then(() => { // Removed response, since it's not being used
          this.successMessage = 'Group created successfully!';
          this.name = '';
          this.description = '';
          this.errorMessage = '';  // Clear any previous error messages
        })
        .catch(error => {
          this.errorMessage = error.response && error.response.data.message ? error.response.data.message : 'An error occurred';
          this.successMessage = '';  // Clear the success message if there's an error
        });
      }
    }
  }
  </script>
  