import { RouteRecordRaw } from 'vue-router';

import ContractorDashboard from './ContractorDashboard.vue'
import ContractorProfile from './ContractorProfile.vue'

const ContractorRoutes: Array<RouteRecordRaw> = [
  {
    path: '/contractor/dashboard',
    name: 'ContractorDashboard',
    component: ContractorDashboard,
  },
  {
    path: '/contractor/profile',
    name: 'ContractorProfile',
    component: ContractorProfile,
  },
];

export default ContractorRoutes;
