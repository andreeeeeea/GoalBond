import { createStore } from 'vuex';
import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = process.env.VUE_APP_API_URL;

export default createStore({
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
      state.isAuthenticated = !!user;
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
        commit('SET_USER', null);
      } catch (error) {
        console.error('Logout error:', error);
      }
    },
    async checkAuth({ commit }) {
      try {
        const response = await axios.get('/check-auth');
        if (response.data.authenticated) {
          commit('SET_USER', response.data.user);
        } else {
          commit('SET_USER', null);
        }
      } catch (error) {
        if (error.response?.status !== 401) {
          console.error('Unexpected authentication error:', error);
        }
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
