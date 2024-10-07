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
      state.user = user
      state.isAuthenticated = !!user
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
        await axios.post('http://localhost:5000/logout')
        commit('SET_USER', null)
      } catch (error) {
        console.error('Logout error:', error)
      }
    },
    async checkAuth({ commit }) {
      try {
        const response = await axios.get('http://localhost:5000/check-auth')
        if (response.data.authenticated) {
          commit('SET_USER', response.data.user)
        } else {
          commit('SET_USER', null)
        }
      } catch (error) {
        console.error('Check auth error:', error)
        commit('SET_USER', null)
      }
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    getUsername: state => state.user ? state.user.username : ''
  }
});