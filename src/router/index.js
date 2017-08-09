import Vue from 'vue'
import VueRouter from 'vue-router'
import RoomList from '../components/RoomList'
import CreateRoom from '../components/CreateRoom'
import Info from '../components/Info'

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
            path: '/createRoom',
            name: 'CreateRoom',
            component: CreateRoom
        },
        {
            path: '/info',
            name: 'Info',
            component: Info
        },
        // {
        //     path: '/room/:id',
        //     component: Room
        // }
    ]
})

export default router
