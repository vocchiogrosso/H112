import { RouteRecordRaw } from 'vue-router';

import UserDashboard from './UserDashboard.vue'
import UserProfile from './UserProfile.vue'

const UserRoutes: Array<RouteRecordRaw> = [
  {
    path: '/user/dashboard',
    name: 'UserDashboard',
    component: UserDashboard,
  },
  {
    path: '/user/profile',
    name: 'UserProfile',
    component: UserProfile,
  },
];

export default UserRoutes;
