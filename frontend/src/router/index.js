import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../components/HomeView.vue';
import LoginView from '../components/LoginForm.vue';
import SignupView from '../components/SignUpForm.vue';
import GoalsList from '@/components/GoalsList.vue';
import GroupView from '@/components/GroupView.vue';
import AccountView from '@/components/AccountView.vue';
import ForgotPassword from '@/components/ForgotPassword.vue';
import ResetPassword from '@/components/ResetPassword.vue';
import ContactView from '@/components/ContactView.vue';
import TermsView from '@/components/TermsView.vue';
import PrivacyView from '@/components/PrivacyView.vue';

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
  },
  {
    path: '/forgot_password',
    name: 'ForgotPassword',
    component: ForgotPassword,
  },
  {
    path: '/reset_password',
    name: 'reset_password',
    component: ResetPassword,
  },
  {
    path: '/group/:groupId/owner',
    name: 'group_owner',
    props: true
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView
  },
  {
    path: '/terms',
    name: 'terms',
    component: TermsView
  },
  {
    path: '/privacy',
    name: 'privacy',
    component: PrivacyView,
  },
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
