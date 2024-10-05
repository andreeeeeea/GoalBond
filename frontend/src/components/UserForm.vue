<template>
    <div>
      <h2>Add User</h2>
      <form @submit.prevent="addUser">
        <input v-model="username" placeholder="Username" required />
        <input v-model="email" type="email" placeholder="Email" required />
        <button type="submit">Add User</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: ''
      };
    },
    methods: {
      async addUser() {
        try {
          const response = await axios.post('http://localhost:5000/users', {
            username: this.username,
            email: this.email
          });
          console.log('User added:', response.data);
          // Clear input fields
          this.username = '';
          this.email = '';
        } catch (error) {
          console.error('Error adding user:', error);
        }
      }
    }
  };
  </script>
  