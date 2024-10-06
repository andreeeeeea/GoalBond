<template>
  <div id="app" class="min-h-screen bg-gray-100 flex flex-col">
    <Navbar />
    <main class="flex-grow p-4">
      <router-view /> <!-- This is where the matched component will be rendered -->
    </main>
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue';
export default {
  name: 'App',
  components: {
    Navbar,
  }
};
</script>

<style>
/* Global styles can go here */
</style>
