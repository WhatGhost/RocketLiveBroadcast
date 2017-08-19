// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '../theme/index.css'
import ElementUI from 'element-ui'
import Vue from 'vue'
import App from './App'
import router from './router/index.js'
import store from './store/store.js'
import './mystyle.css'
import Croppa from 'vue-croppa'
import 'vue-croppa/dist/vue-croppa.css'

Vue.use(Croppa)
Vue.use(ElementUI)
Vue.config.productionTip = false

const v = new Vue({
    el: '#app',
    router,
    store: store,
    template: '<App/>',
    components: {App}
})

v.$store.dispatch('getUserFromDjango')
v.$store.dispatch('getRooms')
