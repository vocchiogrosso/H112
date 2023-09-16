import { RouteRecordRaw } from 'vue-router';

import ManagerDashboard from './ManagerDashboard.vue'
import ManagerProfile from './ManagerProfile.vue'

const ManagerRouter: Array<RouteRecordRaw> = [
  {
    path: '/manager/dashboard',
    name: 'ManagerDashboard',
    component: ManagerDashboard,
  },
  {
    path: '/manager/profile',
    name: 'ManagerProfile',
    component: ManagerProfile,
  },
];

export default ManagerRouter;
