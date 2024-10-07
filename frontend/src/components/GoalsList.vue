<template>
    <div class="goals-list">
        <h2 class="text-2xl font-semibold mb-4">Your Goals</h2>
        <div v-if="goals.length === 0" class="text-gray-700">
            <p>You have no goals added yet.</p>
        </div>
        <ul v-else>
            <li v-for="goal in goals" :key="goal.id" class="mb-4 p-4 border border-gray-300 rounded-lg">
                <h3 class="text-lg font-bold">{{ goal.title }}</h3>
                <p>{{ goal.description }}</p>
                <p>Added: {{ new Date(goal.created_at).toLocaleString('en-US', { 
                    year: 'numeric', 
                    month: '2-digit', 
                    day: '2-digit', 
                    hour: '2-digit', 
                    minute: '2-digit', 
                    hour12: false 
                }) }}</p>
                <p v-if="goal.deadline">Deadline: {{ new Date(goal.deadline).toLocaleString('en-US', { 
                    year: 'numeric', 
                    month: '2-digit', 
                    day: '2-digit', 
                }) }}</p>
                <p>Completed? {{ goal.completed ? 'Yes' : 'No' }}</p>
                <button
                    v-if="!goal.completed" 
                    @click="markAsCompleted(goal.id)"
                    class="mt-2 bg-green-600 text-white py-1 px-4 rounded hover:bg-green-500 transition duration-300"
                >
                    Mark as Completed
                </button>
                <button
                    @click="removeGoal(goal.id)"
                    class="mt-2 bg-red-600 text-white py-1 px-4 rounded hover:bg-red-500 transition duration-300"
                >
                    Remove Goal
                </button>
            </li>
        </ul>
    </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default {
    setup() {
        const store = useStore();
        const goals = ref([]);
        const isAuthenticated = computed(() => store.getters.isAuthenticated);

        const fetchGoals = async () => {
            try {
                const response = await axios.get('http://localhost:5000/goals');
                console.log('Fetched goals:', response.data);
                goals.value = response.data;
            } catch (error) {
                console.error('Error fetching goals:', error);
            }
        };

        const markAsCompleted = async (goalId) => {
            try {
                const response = await axios.put(`http://localhost:5000/goals/${goalId}`, {
                    completed: true,
                });
                console.log('Goal updated:', response.data);
                const goal = goals.value.find(g => g.id === goalId);
                if (goal) {
                    goal.completed = true;
                }
            } catch (error) {
                console.error('Error marking goal as completed:', error);
            }
        };

        const removeGoal = async (goalId) => {
            try {
                const response = await axios.delete(`http://localhost:5000/goals/${goalId}`);
                console.log('Goal removed:', response.data);
                // Remove the goal from the local goals array
                goals.value = goals.value.filter(goal => goal.id !== goalId);
            } catch (error) {
                console.error('Error removing goal:', error);
            }
        };

        onMounted(fetchGoals);

        return {
            goals,
            isAuthenticated,
            markAsCompleted,
            removeGoal,
        };
    },
};
</script>

<style scoped>
/* Add your styles here if needed */
</style>
