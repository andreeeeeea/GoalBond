<template>
  <header class="bg-[#FEFEFD] py-2">
    <div class="container mx-auto flex justify-between items-center">
      <div class="flex items-center space-x-2 mt-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none">
          <path d="M14.7249 8.15612C16.2754 7.23788 17.0507 6.77876 17.6201 7.10452C18.1895 7.43027 18.1758 8.32517 18.1486 10.115L18.1416 10.578C18.1339 11.0866 18.13 11.3409 18.2248 11.5644C18.3196 11.7878 18.5023 11.9552 18.8677 12.2899L19.2003 12.5946C20.4862 13.7725 21.1291 14.3614 20.9784 15.0228C20.8277 15.6841 19.9831 15.9799 18.2941 16.5714L17.8571 16.7245C17.3771 16.8926 17.1371 16.9766 16.953 17.1451C16.7689 17.3137 16.6615 17.5476 16.4467 18.0153L16.2512 18.4412C15.4953 20.0874 15.1174 20.9105 14.4549 20.9935C13.7924 21.0765 13.284 20.3644 12.2673 18.9402L12.0043 18.5717C11.7154 18.167 11.5709 17.9647 11.3623 17.8453C11.1538 17.726 10.9047 17.7032 10.4065 17.6576L9.95303 17.6161C8.20005 17.4557 7.32356 17.3754 7.06482 16.7654C6.80608 16.1553 7.33644 15.4194 8.39716 13.9477L8.67158 13.5669C8.973 13.1487 9.12372 12.9396 9.17893 12.6973C9.23414 12.4551 9.18759 12.2071 9.09451 11.7111L9.00976 11.2596C8.68219 9.51421 8.51841 8.64154 9.02101 8.18152C9.52362 7.7215 10.3598 7.9788 12.032 8.49339L12.4647 8.62652C12.9399 8.77276 13.1775 8.84587 13.4202 8.81547C13.6629 8.78508 13.8832 8.65461 14.3238 8.39368L14.7249 8.15612Z" fill="#1C274C"/>
          <path opacity="0.5" fill-rule="evenodd" clip-rule="evenodd" d="M8.96967 1.96967C9.26256 1.67678 9.73744 1.67678 10.0303 1.96967L12.0303 3.96967C12.3232 4.26256 12.3232 4.73744 12.0303 5.03033C11.7374 5.32322 11.2626 5.32322 10.9697 5.03033L8.96967 3.03033C8.67678 2.73744 8.67678 2.26256 8.96967 1.96967ZM3.46967 3.46967C3.76256 3.17678 4.23744 3.17678 4.53033 3.46967L7.03033 5.96967C7.32322 6.26256 7.32322 6.73744 7.03033 7.03033C6.73744 7.32322 6.26256 7.32322 5.96967 7.03033L3.46967 4.53033C3.17678 4.23744 3.17678 3.76256 3.46967 3.46967ZM12.4697 5.46967C12.7626 5.17678 13.2374 5.17678 13.5303 5.46967L14.0303 5.96967C14.3232 6.26256 14.3232 6.73744 14.0303 7.03033C13.7374 7.32322 13.2626 7.32322 12.9697 7.03033L12.4697 6.53033C12.1768 6.23744 12.1768 5.76256 12.4697 5.46967ZM1.46967 7.46967C1.76256 7.17678 2.23744 7.17678 2.53033 7.46967L3.03033 7.96967C3.32322 8.26256 3.32322 8.73744 3.03033 9.03033C2.73744 9.32322 2.26256 9.32322 1.96967 9.03033L1.46967 8.53033C1.17678 8.23744 1.17678 7.76256 1.46967 7.46967ZM3.96967 9.96967C4.26256 9.67678 4.73744 9.67678 5.03033 9.96967L6.53033 11.4697C6.82322 11.7626 6.82322 12.2374 6.53033 12.5303C6.23744 12.8232 5.76256 12.8232 5.46967 12.5303L3.96967 11.0303C3.67678 10.7374 3.67678 10.2626 3.96967 9.96967Z" fill="#1C274C"/>
        </svg>
        <router-link to="/" class="text-3xl font-bold text-gray-800 hover:text-[#B03052] transition-colors duration-300">
          GoalBond
        </router-link>
      </div>

      <!-- Right-side controls -->
      <div class="flex items-center space-x-6">
      <!-- Authentication buttons -->
        <div class="flex items-center space-x-4">
          <button
            v-if="!isAuthenticated"
            @click="goToLogin"
            class="text-xl font-semibold text-gray-600 px-4 py-2 rounded transition duration-300"
          >
            Login
          </button>
          <button
            v-if="!isAuthenticated"
            @click="goToSignup"
            class="text-xl font-semibold text-gray-600  px-4 py-2 rounded transition duration-300"
          >
            Sign Up
          </button>

          <button
            v-if="isAuthenticated"
            @click="goToGoals"
            class="text-xl text-gray-600 px-4 py-2 rounded transition duration-300"
          >
            Goals
          </button>
          <button
            v-if="isAuthenticated"
            @click="goToAccount"
            class="text-xl text-gray-600  px-4 py-2 rounded transition duration-300"
          >
            Account
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const store = useStore();
    const router = useRouter();

    const isAuthenticated = computed(() => store.getters.isAuthenticated);
    const username = computed(() => store.getters.getUsername || '');

    // Check auth status on component mount
    onMounted(async () => {
      try {
        await store.dispatch('checkAuth');
      } catch (error) {
        console.error('Failed to check authentication:', error);
      }
    });

    const goToProtectedRoute = async (route) => {
      if (!isAuthenticated.value) {
        await store.dispatch('checkAuth');
        if (!isAuthenticated.value) {
          router.push('/login');
          return;
        }
      }
      router.push(route);
    };

    const goToLogin = () => router.push('/login');
    const goToSignup = () => router.push('/signup');
    const goToGoals = () => goToProtectedRoute('/goals');
    const goToGroups = () => goToProtectedRoute('/groups');
    const goToAccount = () => goToProtectedRoute('/account');

    return {
      isAuthenticated,
      username,
      goToLogin,
      goToSignup,
      goToGoals,
      goToGroups,
      goToAccount,
    };
  },
};
</script>

<style scoped>
nav {
  font-family: 'Inter', sans-serif;
}
</style>
