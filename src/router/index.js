import Vue from 'vue'
import VueRouter from 'vue-router'
import RoomList from '../components/RoomList'
import CreateRoom from '../components/CreateRoom'
import Info from '../components/Info'
import PersonalInformation from '../components/PersonalInformation'
import ChangeNickname from '../components/ChangeNickname'
import ChangePassword from '../components/ChangePassword'
import LiveRoom from '../components/LiveRoom'

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
            component: Info,
            children: [
                {
                    path: 'personalInformation',
                    component: PersonalInformation
                },
                {
                    path: 'changeNickname',
                    component: ChangeNickname
                },
                {
                    path: 'changePassword',
                    component: ChangePassword
                }
            ]
        },
        {
            path: '/room/:id',
            component: LiveRoom
        }
    ]
})

export default router
