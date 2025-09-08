
<template>
    <div class="items-center justify-center py-12 px-4">
      <div class="w-96 mx-auto py-32">
        <div v-if="tokenValid">
          <h1 class="text-2xl font-bold text-center">Reset Password</h1>
          <form @submit.prevent="resetPassword" class="mt-10">
            <div class="mb-4">
              <label for="password" class="block mb-2">New Password:</label>
              <input 
                v-model="password" 
                type="password" 
                placeholder="Enter new password" 
                required 
                minlength="6"
                :disabled="loading"
                class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052] disabled:opacity-50" 
              />
            </div>
            <div class="mb-4">
              <label for="confirmPassword" class="block mb-2">Confirm Password:</label>
              <input 
                v-model="confirmPassword" 
                type="password" 
                placeholder="Confirm new password" 
                required 
                minlength="6"
                :disabled="loading"
                class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#B03052] disabled:opacity-50" 
              />
            </div>
            <button 
              type="submit" 
              :disabled="loading"
              class="w-full bg-[#B03052] text-white font-bold py-2 px-4 rounded-lg hover:bg-[#8B2440] transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ loading ? 'Resetting...' : 'Reset Password' }}
            </button>
          </form>
        </div>
        <div v-else class="text-center">
          <h1 class="text-2xl font-bold mb-4">Invalid or Expired Link</h1>
          <p class="text-gray-600 mb-4">This password reset link is invalid or has expired.</p>
          <router-link to="/forgot_password" class="text-[#B03052] hover:text-[#8B2440]">Request a new password reset link</router-link>
        </div>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';
import { useToast } from 'vue-toastification';

export default {
  setup() {
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      password: '',
      confirmPassword: '',
      loading: false,
      tokenValid: true,
    };
  },
  methods: {
    async resetPassword() {
      // Validate passwords match
      if (this.password !== this.confirmPassword) {
        this.toast.error('Passwords do not match');
        return;
      }

      if (this.password.length < 6) {
        this.toast.error('Password must be at least 6 characters long');
        return;
      }

      const token = this.$route.query.token;
      if (!token) {
        this.toast.error('Invalid reset link');
        this.tokenValid = false;
        return;
      }

      this.loading = true;
      try {
        const response = await axios.post(`/reset_password/${token}`, {
          password: this.password
        });

        if (response.data.success) {
          this.toast.success('Password reset successfully! Redirecting to login...');
          this.password = '';
          this.confirmPassword = '';
          // Redirect to login after success
          setTimeout(() => {
            this.$router.push('/login');
          }, 2000);
        } else {
          this.toast.error(response.data.message || 'Failed to reset password');
          if (response.data.message?.includes('expired') || response.data.message?.includes('invalid')) {
            this.tokenValid = false;
          }
        }
      } catch (error) {
        console.error('Reset password error:', error);
        if (error.response?.status === 400) {
          this.toast.error('This reset link has expired or is invalid');
          this.tokenValid = false;
        } else {
          this.toast.error(error.response?.data?.message || 'An error occurred. Please try again.');
        }
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    // Check if token exists
    const token = this.$route.query.token;
    if (!token) {
      this.tokenValid = false;
      this.toast.error('No reset token provided');
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
  