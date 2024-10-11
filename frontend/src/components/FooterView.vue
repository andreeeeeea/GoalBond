<template>
    <footer class="bg-teal-600 text-white py-6 mt-10">
      <div class="container mx-auto text-center">
        <div class="flex justify-center space-x-4 mb-4">
          <a href="#" class="hover:underline">Privacy Policy</a>
          <a href="#" class="hover:underline">Terms of Service</a>
          <a href="#" class="hover:underline">Contact Us</a>
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
  footer {
    background-color: #1f2937; /* Dark background */
  }
  
  footer a {
    color: #ffffff; /* White text */
    transition: color 0.3s ease;
  }
  
  footer a:hover {
    color: #86efac; /* Light green on hover */
  }
  </style>
  