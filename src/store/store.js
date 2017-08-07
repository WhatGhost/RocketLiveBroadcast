import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'
import user from './user.js'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000' // This will change if you deploy later

const store = new Vuex.Store({
    state: {
        rooms: [],
        account: ''
    },
    mutations: {
        // Keep in mind that response is an HTTP response
        // returned by the Promise.
        // The mutations are in charge of updating the client state.
        'GET_ROOMS': function (state, response) {
            state.rooms = response.body
        },
        'ADD_ROOM': function (state, response) {
            state.rooms.push(response.body)
        },
        'CLEAR_ROOMS': function (state) {
            const rooms = state.rooms
            rooms.splice(0, rooms.length)
        },
        // Note that we added one more for logging out errors.
        'API_FAIL': function (state, error) {
            console.error(error)
        },
        'API_SUCC': function (state) {
        },
        'SUCC_LOGIN': function (state, response) {
            state.account = response.body
        },
    },
    actions: {
        // We added a getRooms action for the initial load from the server
        // These URLs come straight from the Django URL router we did in Part 3
        getRooms(store) {
            return api.get(apiRoot + '/rooms/')
                .then((response) => store.commit('GET_ROOMS', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        addRoom(store, room) {
            return api.post(apiRoot + '/rooms/', room)
                .then((response) => store.commit('ADD_ROOM', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        clearRooms(store) {
            return api.delete(apiRoot + '/rooms/clear_rooms/')
                .then((response) => store.commit('CLEAR_ROOMS'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        loginUser(store, userinfo) {
            return user.post(apiRoot + '/users/login_users/', userinfo)
                .then((response) => store.commit('SUCC_LOGIN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        registerUser(store, userinfo) {
            return user.post(apiRoot + '/users/', userinfo)
                .then((response) => store.commit('API_SUCC', userinfo))
                .catch((error) => store.commit('API_FAIL', error))
        },
        changeNick(store, userinfo) {
            userinfo.account = store.state.account
            return user.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        changePasswd(store, userinfo) {
            return user.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
    }
})

export default store
