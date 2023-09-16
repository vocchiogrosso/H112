import { RouteRecordRaw } from 'vue-router';

import ContractorDashboard from './ContractorDashboard.vue'
import ContractorNavigation from './ContractorNavigation.vue'
import ContractorProfile from './ContractorProfile.vue'

const ContractorRoutes: Array<RouteRecordRaw> = [
  {
    path: '/contractor/dashboard',
    name: 'ContractorDashboard',
    component: ContractorDashboard,
  },
  {
    path: '/contractor/navigation/:shipment._id',
    name: 'ContractorNavigation',
    component: ContractorNavigation,
    props: true
  },
  {
    path: '/contractor/profile',
    name: 'ContractorProfile',
    component: ContractorProfile,
  },
];

export default ContractorRoutes;
