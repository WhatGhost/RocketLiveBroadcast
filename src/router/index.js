import Vue from 'vue'
import VueRouter from 'vue-router'
import RoomList from '../components/RoomList'
import LiveRoom from '../components/LiveRoom'
import Forget from '../components/Forget'

Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        { path: '/', redirect: '/roomList' },
        {
            path: '/roomList',
            name: 'RoomList',
            component: RoomList
        },
        {
            path: '/room/:id',
            component: LiveRoom
        },
        {
            path: '/forget',
            component: Forget
        }
    ]
})

export default router
