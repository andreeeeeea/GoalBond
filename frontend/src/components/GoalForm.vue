<template>
    <div>
      <h2>Add Goal</h2>
      <form @submit.prevent="addGoal">
        <input v-model="title" placeholder="Goal Title" required />
        <textarea v-model="description" placeholder="Description"></textarea>
        <input v-model="userId" type="number" placeholder="User ID" required />
        <button type="submit">Add Goal</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: '',
        description: '',
        userId: ''
      };
    },
    methods: {
      async addGoal() {
        try {
          const response = await axios.post('http://localhost:5000/goals', {
            title: this.title,
            description: this.description,
            user_id: this.userId
          });
          console.log('Goal added:', response.data);
          // Clear input fields
          this.title = '';
          this.description = '';
          this.userId = '';
        } catch (error) {
          console.error('Error adding goal:', error);
        }
      }
    }
  };
  </script>
  