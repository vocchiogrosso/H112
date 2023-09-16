import { RouteRecordRaw } from 'vue-router';

import Home from './Home.vue'
import Auth from './Auth.vue'

const SharedRoutes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
];

export default SharedRoutes;