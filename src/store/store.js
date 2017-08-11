import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'
import router from '../router/index.js'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000' // This will change if you deploy later

const store = new Vuex.Store({
    state: {
        rooms: [],
        live_room_id: -1,
        account: null,
        nickname: null,
        isTeacher: false,
        // background blur flag
        background_blur: false,
        showRegister: false,
        showLogin: false,
        showForget: false,
        // 完成幻灯片上传
        finishSlideUpload: false,
        // 上传凭证
        token: '',
        // 服务端文件名称
        slideKey: ''
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
        'GET_ROOM_ID': function (state, response) {
            console.log(response.body)
            state.live_room_id = response.body.id
            console.log(state.live_room_id)
        },
        'API_FAIL': function (state, error) {
            window.alert('失败')
            console.error(error)
        },
        'Register_SUCC': function (state) {
            console.log(state)
            window.alert('成功！')
            state.showLogin = true
            state.showRegister = false
        },
        'API_SUCC': function (state) {
            console.log(state)
            window.alert('成功！')
        },
        'LOGOUT_SUCC': function (state) {
            console.log(state)
            window.alert('登出成功！')
            state.account = null
            state.nickname = null
            state.isTeacher = false
            router.push('/roomList')
        },
        'SUCC_LOGIN': function (state, response) {
            window.alert('登陆成功')
            console.log(response)
            state.account = response.body['account']
            state.nickname = response.body['nickname']
            state.background_blur = false
            state.showLogin = false
            router.push('/roomList')
        },
        trueBlur: function (state) {
            state.background_blur = true
        },
        falseBlur: function (state) {
            state.background_blur = false
        },
        trueRegister: function (state) {
            state.showRegister = true
        },
        falseRegister: function (state) {
            state.showRegister = false
        },
        trueLogin: function (state) {
            state.showLogin = true
        },
        falseLogin: function (state) {
            state.showLogin = false
        },
        trueForget: function (state) {
            state.showForget = false
        },
        falseForget: function (state) {
            state.showForget = false
        },
        finishSlideUpload: function (state) {
            state.finishSlideUpload = true
        },
        getUser: function (state, response) {
            if (response.body.account) {
                state.account = response.body['account']
                state.nickname = response.body['nickname']
                state.isTeacher = response.body['isTeacher']
            } else {
                state.account = null
                state.nickname = null
                state.isTeacher = false
            }
        },
        gotToken: function (state, response) {
            state.token = response.body['token']
            state.slideKey = response.body['key']
        },
        gotTokenFail: function (state, response) {
            state.token = ''
            state.slideKey = ''
        }
    },
    actions: {
        // We added a getRooms action for the initial load from the server
        // These URLs come straight from the Django URL router we did in Part 3
        getRooms(store) {
            return api.get(apiRoot + '/liveroom/')
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
            return api.post(apiRoot + '/users/login_users/', userinfo)
                .then((response) => store.commit('SUCC_LOGIN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        registerUser(store, userinfo) {
            console.log(userinfo)
            return api.post(apiRoot + '/users/', userinfo)
                .then((response) => store.commit('Register_SUCC', userinfo))
                .catch((error) => store.commit('API_FAIL', error))
        },
        changeNick(store, userinfo) {
            userinfo.account = store.state.account
            return api.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        changePasswd(store, userinfo) {
            return api.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        createRoom(store, formData) {
            return api.post(apiRoot + '/liveroom/', formData)
                .then((response) => store.commit('GET_ROOM_ID', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        sendVertificateCode(store, vertificateInfo) {
            console.log('dispatched')
            return api.post(apiRoot + '/users/sendVertificateCode/', vertificateInfo)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        forgetPassword(store, info) {
            console.log('dispathed')
            return api.patch(apiRoot + '/users/forget_info/', info)
                .then((response) => store.commit('API_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        logout(store) {
            console.log('dispathed')
            return api.post(apiRoot + '/users/logout_user/')
                .then((response) => store.commit('LOGOUT_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        askToken(store, fileName) {
            return api.post(apiRoot + '/slide/askToken', fileName)
                .then((response) => store.commit('gotToken', response))
                .catch((error) => store.commit('gotTokenFail', error))
        },
        openRegisterDialog: function () {
            store.commit('trueRegister')
            store.commit('trueBlur')
        },
        closeRegisterDialog: function () {
            store.commit('falseRegister')
            store.commit('falseBlur')
        },
        openLoginDialog: function () {
            store.commit('trueLogin')
            store.commit('trueBlur')
        },
        openForget: function () {
            store.commit('trueForget')
            store.commit('trueBlur')
        },
        closeForget: function () {
            store.commit('closeForget')
            store.commit('closeBlur')
        },
        closeLoginDialog: function () {
            console.log('commiting')
            store.commit('falseLogin')
            store.commit('falseBlur')
        },
        endUploadingSlide: function () {
            store.commit('finshSlideUpload')
        },
        getUserFromDjango: function () {
            return api.post(apiRoot + '/users/current_user/')
                .then((response) => store.commit('getUser', response))
                .catch((error) => store.commit('API_FAIL', error))
        }
    }
})

export default store
