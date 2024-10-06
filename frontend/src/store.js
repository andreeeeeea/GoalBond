import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthenticated: false, // Set initial authentication state
    user: null, // Add user data state
  },
  mutations: {
    SET_AUTH(state, user) {
      state.isAuthenticated = true; // Set to true on login
      state.user = user; // Store user info
    },
    logout(state) {
      state.isAuthenticated = false; // Set to false on logout
      state.user = null; // Clear user info
    },
    SET_USER_FROM_STORAGE(state, user) {
      state.isAuthenticated = true;
      state.user = user;
    },
  },
  actions: {
    login({ commit }, user) {
      commit('SET_AUTH', user); // Commit mutation with user info
      localStorage.setItem('user', JSON.stringify(user)); // Save user data in localStorage
    },
    logout({ commit }) {
      commit('logout'); // Just commit the logout mutation
      localStorage.removeItem('user'); // Clear user info from local storage
    },
    setUserFromStorage({ commit }) {
      const user = JSON.parse(localStorage.getItem('user'));
      if (user) {
        commit('SET_USER_FROM_STORAGE', user); // Set user data from localStorage
      }
    },
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated; // Getter for authentication state
    },
    getUser(state) {
      return state.user; // Getter for user info
    },
    getUsername(state) {
      return state.user ? state.user.username : ''; // Getter for user's username
    },
  },
});
