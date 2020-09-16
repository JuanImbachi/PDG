import Vue from 'vue'
import App from './App'
import router from './routes/router'
import vuetify from './plugins/vuetify';
import VueGeolocation from 'vue-browser-geolocation'

Vue.config.productionTip = false
Vue.use(VueGeolocation)

import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAg7Sa9QNBaUTcivKeUdoZmKCenigt_f1c'
  },
  installComponents: false
})

Vue.component('google-map', VueGoogleMaps.Map);

new Vue({
  el: '#app',
  router,
  components: { App },
  vuetify,
  template: '<App/>'
})
