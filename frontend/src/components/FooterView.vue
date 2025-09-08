<template>
    <footer class=" text-gray-900 py-6 mt-10">
      <div class="container mx-auto text-center">
        <div class="flex justify-center space-x-4 mb-4">
          <a href="/privacy" class="hover:underline">Privacy Policy</a>
          <a href="/terms" class="hover:underline">Terms of Service</a>
          <a href="/contact" class="hover:underline">Contact Us</a>
        </div>
        <div>
          <p class="text-sm">Made with ❤️ by Andreea</p>
        </div>
        <p class="mt-4 text-xs">&copy; {{ currentYear }} GoalBond. All rights reserved.</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'FooterView',
    computed: {
      currentYear() {
        return new Date().getFullYear();
      }
    }
  };
  </script>
  
  <style scoped>

  </style>
  