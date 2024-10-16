import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../components/HomeView.vue';
import LoginView from '../components/LoginForm.vue';
import SignupView from '../components/SignUpForm.vue';
import GoalsList from '@/components/GoalsList.vue';
import GroupView from '@/components/GroupView.vue';
import AccountView from '@/components/AccountView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/goals',
    name: 'goals',
    component: GoalsList,
    meta: { requiresAuth: true }, // Protect this route
  },
  {
    path: '/groups',
    name: 'groups',
    component: GroupView,
    meta: { requiresAuth: true }, // Protect this route
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView,
    meta: { requiresAuth: true }, // Protect this route
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Route Guard
router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('user') !== null; // Check if user is authenticated

  if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
    next({ name: 'login' }); // Redirect to login if not authenticated
  } else {
    next();
  }
});

export default router;
