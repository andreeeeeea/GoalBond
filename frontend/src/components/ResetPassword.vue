
<template>
    <div class="items-center justify-center py-12 px-4">
      <div class="w-96 mx-auto py-32">
        <h1 class="text-2xl font-bold text-center">Reset Password</h1>
        <form @submit.prevent="resetPassword" class="mt-10">
          <div class="mb-4">
            <input 
              v-model="password" 
              type="password" 
              placeholder="Enter new password" 
              required 
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" 
            />
          </div>
          <button 
            type="submit" 
            class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-500 transition duration-300"
          >
            Reset Password
          </button>
        </form>
      </div>

    </div>
  </template>
  
<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

  export default {
    data() {
      return {
        password: '',
      };
    },
    methods: {
        async resetPassword() {
            const token = this.$route.query.token;
            try {
            const response = await axios.post(`/reset_password/${token}`, {
                password: this.password
            });

            if (response.data.success) {
                this.toast.success(response.data.message);
                this.password = ''; 
            } else {
                this.toast.error(response.data.message);
            }
            } catch (error) {
              this.toast.error('An error occurred. Please try again.');
            }
        }
    },
    mounted() {
        this.toast = useToast();
    }
  };
</script>

<style>
.success {
  color: green;
}

.error {
  color: red;
}
</style>
  