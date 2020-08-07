import Vue from 'vue'
import App from './App'
import router from './routes/router'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  vuetify,
  template: '<App/>'
})
