import { RouteRecordRaw } from 'vue-router';

import Auth from './Auth.vue'

const SharedRoutes: Array<RouteRecordRaw> = [
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
  },
];

export default SharedRoutes;