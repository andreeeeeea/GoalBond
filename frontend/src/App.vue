<template>
  <notifications group="foo" />
  <div id="app" class="min-h-screen bg-[#FEFEFD] flex flex-col">
    <Navbar/>
    <main class="flex-grow pt-4">
      <router-view />
    </main>
    <Footer />
    <AddButton  />
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue';
import Footer from './components/FooterView.vue';
import AddButton from './components/AddButton.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
    AddButton,
  },
};
</script>

<style>
/* Global styles can go here */
</style>