import { RouteRecordRaw } from 'vue-router';

import Home from './Home.vue'
import Login from './Login.vue'
import Register from './Register.vue'

const SharedRoutes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/auth/login',
    name: 'LoginVue',
    component: Login,
  },
  {
    path: '/auth/register',
    name: 'RegisterVue',
    component: Register,
  },
];

export default SharedRoutes;