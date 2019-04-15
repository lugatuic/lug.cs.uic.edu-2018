import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home';
import Projects from '@/views/Projects';
import Wiki from '@/views/Wiki';
import Events from '@/views/Events';
import Services from '@/views/Services';
import OfficePolicy from '@/views/OfficePolicy';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // TODO: decide how many, if any, routes should be dynamically loaded
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/projects',
      name: 'Projects',
      component: Projects,
    },
    {
      path: '/wiki',
      name: 'Wiki',
      component: Wiki,
    },
    {
      path: '/events',
      name: 'Events',
      component: Events,
    },
    {
      path: '/services',
      name: 'Services',
      component: Services,
    },
    {
      path: '/office-policy',
      name: 'Office Policy',
      component: OfficePolicy,
    },
  ],
});
