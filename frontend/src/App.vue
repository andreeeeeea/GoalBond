<template>
  <div id="app">
    <h1>Goal Tracker</h1>
    <UserForm />
    <GoalForm />
  </div>
</template>

<script>
import UserForm from './components/UserForm.vue';
import GoalForm from './components/GoalForm.vue';

export default {
  components: {
    UserForm,
    GoalForm
  }
};
</script>

<style>
/* Add your styles here */
</style>
