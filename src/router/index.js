import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/store.js'
import RoomList from '../components/RoomList'
import LiveRoom from '../components/LiveRoom'
import HistoryVideo from '../components/HistoryVideo'

Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        {path: '/', redirect: '/roomList'},
        {
            path: '/roomList',
            name: 'RoomList',
            component: RoomList,
        },
        {
            path: '/room/:id',
            component: LiveRoom,
            beforeEnter: function (to, from, next) {
                store.dispatch('getUserFromDjango').then(() => {
                    store.dispatch('getRooms').then(() => {
                        if (store.state.account === null) {
                            next(false)
                            return
                        }
                        let roomId = parseInt(to.params['id'])
                        for (let room of store.state.rooms) {
                            if (room.id === roomId) {
                                next()
                                return
                            }
                        }
                        next(false)
                    })
                })
            }
        },
        {
            path: '/history/:id',
            component: HistoryVideo,
            beforeEnter: function (to, from, next) {
                if (store.state.account === null) {
                    next(false)
                    return
                }
                next()
            }
        }
    ]
})

export default router
