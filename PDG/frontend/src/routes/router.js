import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home'
import Test from '../components/Test'
import Login from '../components/Login'
import Comuna from '../components/Comuna'
Vue.use(Router);

export default new Router({
  mode : 'history',
  routes: [
    {path: '/', component: Home},
    {path: '/test', component: Test},
    {path:'/login', component: Login},
    {path:'/comuna/:id', component: Comuna}
  ]
});
