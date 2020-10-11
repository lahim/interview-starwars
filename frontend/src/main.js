import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'

import router from "@/routes";

import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'


Vue.config.productionTip = false

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(require('vue-moment'))
Vue.use(VueRouter)



new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
