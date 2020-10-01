import Vue from 'vue';
import Router from 'vue-router';
import Home from '../components/Home'
import Data from '../components/Data'
import Login from '../components/Login'
import Prediction from '../components/Prediction'
Vue.use(Router);

export default new Router({
  mode : 'history',
  routes: [
    {path: '/', component: Home},
    {path: '/data', component: Data},
    {path:'/login', component: Login},
    {path:'/predictions', component: Prediction}
  ]
});
