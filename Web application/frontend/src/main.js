import Vue from 'vue'
import App from './App'
import router from './routes/router'
import vuetify from './plugins/vuetify';
import VueGoogleHeatmap from 'vue-google-heatmap';


Vue.use(VueGoogleHeatmap,  {
  apiKey: '[INSERT YOUR API KEY]'
});

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  vuetify,
  template: '<App/>'
})
