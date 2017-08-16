// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import '../theme/index.css'
import ElementUI from 'element-ui'
import Vue from 'vue'
import App from './App'
import router from './router/index.js'
import store from './store/store.js'
import './mystyle.css'

Vue.use(ElementUI)
Vue.config.productionTip = false

// Vue.http.interceptors.push(function (request, next) {
//     // 跨域携带cookie
//     request.credentials = true
//     next()
// })

// function strTrim(name) {
//     return name.replace(/(^\s*)|(\s*$)/g, '')
// }

// function getCookie(name) {
//     var cookieValue = null
//     // console.log(document.cookie)
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';')
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = strTrim(cookies[i])
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
//                 break
//             }
//         }
//     }
//     console.log('this is ' + cookieValue)
//     return cookieValue
// }

// Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken')

/* eslint-disable no-new */
const v = new Vue({
    el: '#app',
    router,
    store: store,
    template: '<App/>',
    components: {App}
})

v.$store.dispatch('getUserFromDjango')
v.$store.dispatch('getRooms')
