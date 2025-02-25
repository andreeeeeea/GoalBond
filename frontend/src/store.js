import { createStore } from 'vuex';
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000'; // Set the base URL for all requests

export default createStore({
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      state.isAuthenticated = !!user;  // Set authentication status
      console.log('Setting isAuthenticated to:', state.isAuthenticated);
    }
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post('/login', credentials);
        commit('SET_USER', response.data.user);
        return response;
      } catch (error) {
        console.error('Login error:', error);
        throw error;
      }
    },
    async logout({ commit }) {
      try {
        await axios.post('/logout');
        commit('SET_USER', null); // Clear user data on logout
      } catch (error) {
        console.error('Logout error:', error);
      }
    },
    async checkAuth({ commit }) {
      try {
        const response = await axios.get('/check-auth');
        if (response.data.authenticated) {
          commit('SET_USER', response.data.user); // Update user data if authenticated
        } else {
          commit('SET_USER', null);
        }
      } catch (error) {
        console.error('Check auth error:', error);
        commit('SET_USER', null);
      }
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    getUsername: state => (state.user ? state.user.username : ''),
    getEmail: state => (state.user ? state.user.email : ''), // Add a getter for email
    getNickname: state => (state.user ? state.user.nickname : ''),
    currentUser: state => state.user
  }
});
