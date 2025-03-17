
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
        <div class="my-4 flex items-center justify-center">
            <p v-if="message" :class="messageClass" class="mt-2 text-center">{{ message }}</p>
        </div>
      </div>

    </div>
  </template>
  
<script>
import axios from 'axios';

  export default {
    data() {
      return {
        password: '',
        message: '',
        messageClass: ''
      };
    },
    methods: {
        async resetPassword() {
            const token = this.$route.query.token;
            console.log("hewwo", this.$route.query.token); 
            try {
            const response = await axios.post(`/reset_password/${token}`, {
                password: this.password
            });

            if (response.data.success) {
                this.message = response.data.message;
                this.messageClass = 'success';
                this.password = ''; 
            } else {
                this.errorMessage = response.data.message;
                this.messageClass = 'error';
            }
            } catch (error) {
            console.error('Password reset failed:', error);
            this.message = 'An error occurred. Please try again.';
            this.messageClass = 'error';
            }
        }
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
  