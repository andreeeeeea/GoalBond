import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; 
import './assets/output.css'; 
import store from './store'; 
import axios from 'axios';
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";


axios.defaults.withCredentials = true;
axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.baseURL = process.env.VUE_APP_API_URL || 'http://127.0.0.1:5000/';

const app = createApp(App);
app.config.globalProperties.$axios = axios;

const options = {
  // You can set your default options here
};

app.use(Toast, options);


// Check authentication status before mounting the app
store.dispatch('checkAuth').then(() => {
  app.use(store).use(router).mount('#app')
});

