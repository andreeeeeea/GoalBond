<template>
  <div id="app" class="min-h-screen bg-gray-100 flex flex-col">
    <Navbar />
    <main class="flex-grow pt-4">
      <router-view /> <!-- This is where the matched component will be rendered -->
    </main>
    <Footer /> <!-- Add the Footer component here -->
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue';
import Footer from './components/FooterView.vue'; // Import the Footer component

export default {
  name: 'App',
  components: {
    Navbar,
    Footer, // Register the Footer component
  }
};
</script>

<style>
/* Global styles can go here */
</style>
