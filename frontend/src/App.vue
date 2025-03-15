<template>
  <notifications group="foo" />
  <div id="app" class="min-h-screen bg-gray-100 flex flex-col">
    <Navbar />
    <main class="flex-grow pt-4">
      <router-view /> 
    </main>
    <Footer /> 
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue';
import Footer from './components/FooterView.vue'; 

export default {
  name: 'App',
  components: {
    Navbar,
    Footer, 
  }
};
</script>

<style>
/* Global styles can go here */
</style>
