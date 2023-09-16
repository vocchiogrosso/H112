import { RouteRecordRaw } from 'vue-router';

import UserDashboard from './UserDashboard.vue'
import UserProfile from './UserProfile.vue'
import RequestForm from './RequestForm.vue';

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
  {
    path: '/user/request-form',
    name: 'RequestForm',
    component: RequestForm, // Import and use your RequestForm component
  }
];

export default UserRoutes;
