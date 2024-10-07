<template>
    <div class="flex flex-wrap -mx-4">
      <div class="w-full md:w-1/2 p-4">
        <h2 class="text-2xl font-semibold mb-4">Personal Goals</h2>
        <div v-if="goals.filter(goal => !goal.is_group_goal).length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="goal in goals.filter(goal => !goal.is_group_goal)" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-56">
            <div class="flex-grow">
              <p>{{ goal.description }}</p>
              <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleString() }}</span>
              <p>Status: {{ goal.completed ? 'Completed' : 'To Do' }}</p>
            </div>
            <div class="mt-auto">
              <button v-if="!goal.completed" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
              <button v-else class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Re-do Goal</button>
              <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
            </div>
          </div>
        </div>
        <div v-else class="text-center">
          <p>No personal goals found. Start by creating one!</p>
        </div>
      </div>
      <div class="w-full md:w-1/2 p-4">
        <h2 class="text-2xl font-semibold mb-4">Group Shared Goals</h2>
        <div v-if="goals.filter(goal => goal.is_group_goal).length > 0" class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div v-for="goal in goals.filter(goal => goal.is_group_goal)" :key="goal.id" class="bg-white rounded-lg shadow p-4 flex flex-col h-56">
            <div class="flex-grow">
              <h3 class="text-lg font-semibold">{{ goal.title }}</h3>
              <p>{{ goal.description }}</p>
              <span v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleString() }}</span>
              <p>Status: {{ goal.completed ? 'Completed' : 'To Do' }}</p>
              <p>Group: {{ goal.group.name }}</p>
              <p>Members: 
                <span v-for="member in goal.group.members" :key="member.id">{{ member.username }}<span v-if="!$last">, </span></span>
              </p>
            </div>
            <div class="mt-auto">
              <button v-if="!goal.completed" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Toggle Completion</button>
              <button v-else class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" @click="toggleGoalCompletion(goal)">Re-do Goal</button>
              <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="deleteGoal(goal.id)">Delete Goal</button>
            </div>
          </div>
        </div>
        <div v-else class="text-center">
          <p>No group shared goals found. Start by creating one!</p>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        goals: [],
        newGoal: {
          title: '',
          description: '',
          deadline: '',
          group_id: null,  // Set to null for personal goals
        },
        groups: []  // To hold the list of groups for selection
      };
    },
    mounted() {
      this.fetchGoals();
      this.fetchGroups();
    },
    methods: {
      async fetchGoals() {
        try {
          const response = await axios.get('/goals');
          this.goals = response.data;
        } catch (error) {
          console.error("Error fetching goals:", error);
        }
      },
      async fetchGroups() {
        try {
          const response = await axios.get('/groups');  // Adjust this endpoint as necessary
          this.groups = response.data;
        } catch (error) {
          console.error("Error fetching groups:", error);
        }
      },
      async createGoal() {
        try {
          await axios.post('/goals', this.newGoal);
          this.fetchGoals();  // Refresh the goals list
          this.resetNewGoal();
        } catch (error) {
          console.error("Error creating goal:", error);
        }
      },
      async toggleGoalCompletion(goal) {
        try {
          await axios.put(`/goals/${goal.id}`, {
            completed: !goal.completed
          });
          this.fetchGoals();  // Refresh the goals list
        } catch (error) {
          console.error("Error updating goal completion:", error);
        }
      },
      async deleteGoal(goalId) {
        try {
          await axios.delete(`/goals/${goalId}`);
          this.fetchGoals();  // Refresh the goals list
        } catch (error) {
          console.error("Error deleting goal:", error);
        }
      },
      resetNewGoal() {
        this.newGoal = {
          title: '',
          description: '',
          deadline: '',
          group_id: null,
        };
      },
    }
  };
  </script>
  
  <style scoped>
  /* Add any styles here for better presentation */
  h1 {
    color: #333;
  }
  form {
    margin-bottom: 20px;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ccc;
  }
  </style>
  