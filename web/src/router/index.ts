import { createRouter, createWebHistory } from 'vue-router';

import ContractorRoutes from '../views/contractor/ContractorRouter'
import ManagerRoutes from '../views/manager/ManagerRouter';
import SharedRoutes from '../views/shared/SharedRouter'
import UserRoutes from '../views/user/UserRouter'

const routes = [
  ...ContractorRoutes,
  ...ManagerRoutes,
  ...SharedRoutes,
  ...UserRoutes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
