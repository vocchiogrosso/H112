import { createRouter, createWebHistory } from 'vue-router';

import ContractorRoutes from '../views/contractor/ContractorRouter'
//import ManagerRoutes from '../views/manager/ManagerRouter';
import SharedRoutes from '../views/shared/SharedRouter'
import UserRoutes from '../views/user/UserRouter'
import Auth from "../views/shared/Auth.vue";

const routes = [
  ...ContractorRoutes,
  //...ManagerRoutes,
  ...SharedRoutes,
  ...UserRoutes,
  {path: '/', component: Auth}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
