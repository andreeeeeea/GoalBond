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
  position: "bottom-left",
  timeout: 3000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: "button",
  icon: true,
  rtl: false
};

app.use(Toast, options);


// Check authentication status before mounting the app
store.dispatch('checkAuth').then(() => {
  app.use(store).use(router).mount('#app')
});

