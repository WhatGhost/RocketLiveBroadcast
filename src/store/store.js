import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'
import router from '../router/index.js'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000' // This will change if you deploy later
/**
 * This module contains classes for running a store.
 * @module Store
 */
const store = new Vuex.Store({
    /**
     * @class state
     * @type Object
     */
    state: {
        // 所有房间列表
        /**
         * @property rooms
         * @type Object
         */
        rooms: [],
        // 所有历史记录
        history: [],
        // 当前用户身份信息
        /**
         * @property account
         * @type String
         * @default "null"
         */
        account: null,
        /**
         * @property nickname
         * @type String
         * @default "null"
         */
        nickname: null,
        /**
         * @property isTeacher
         * @type Boolean
         * @default "false"
         */
        isTeacher: false,
        // 控制背景虚化，用于配合弹出窗口
        /**
         * @property background_blur
         * @type Boolean
         * @default "false"
         */
        background_blur: false,
        // 五种弹出模式窗口
        /**
         * @property showRegister
         * @type Boolean
         * @default "false"
         */
        showRegister: false,
        /**
         * @property showLogin
         * @type Boolean
         * @default "false"
         */
        showLogin: false,
        /**
         * @property showForget
         * @type Boolean
         * @default "false"
         */
        showForget: false,
        /**
         * @property showInfo
         * @type Boolean
         * @default "false"
         */
        showInfo: false,
        /**
         * @property showCreateRoom
         * @type Booleaan
         * @default "false"
         */
        showCreateRoom: false,
    },
    mutations: {
        /**
         * 获取房间到房间列表
         *
         *
         * @method GET_ROOMS
         * @param state {Object} An `state` Object
         * @param response {object} Get data object
         * @chainable
         */
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
        /**
         * 获取房间的ID
         *
         *
         * @method GET_ROOM_ID
         * @param state {Object} An `state` Object
         * @param response {object} Get data object
         * @chainable
         */
        'GET_ROOM_ID': function (state, response) {
            state.live_room_id = response.body.id
        },
        /**
         * 处理与后端通信时出现的错误
         *
         *
         * @method API_FAIL
         * @param state {Object} An `state` Object
         * @param error {object} Response an error
         * @chainable
         */
        'API_FAIL': function (state, error) {
            Vue.prototype.$message({
                message: error.body.detail,
                type: 'error',
            })
            console.error(error)
        },
        /**
         * 处理成功注册的函数
         *
         *
         * @method Register_SUCC
         * @param state {Object} An `state` Object
         * @chainable
         */
        'Register_SUCC': function (state) {
            Vue.prototype.$message({
                message: '注册成功！',
                type: 'success',
            })
            state.showLogin = true
            state.showRegister = false
        },
        /**
         *  处理与后端通信时成功
         *
         *
         * @method API_SUCC
         * @param state {Object} An `state` Object
         * @chainable
         */
        'API_SUCC': function (state, response) {
            Vue.prototype.$message({
                message: response.body.detail,
                type: 'success',
            })
        },
        /**
         *  处理成功登出的函数
         *
         *
         * @method LOGOUT_SUCC
         * @param state {Object} An `state` Object
         * @chainable
         */
        'LOGOUT_SUCC': function (state) {
            Vue.prototype.$message({
                message: '登出成功！',
                type: 'success',
            })
            state.account = null
            state.nickname = null
            state.isTeacher = false
            router.push('/roomList')
        },
        /**
         *  处理成功登录的函数，获取账户以及用户昵称
         *
         *
         * @method SUCC_LOGIN
         * @param state {Object} An `state` Object
         * @chainable
         */
        'SUCC_LOGIN': function (state, response) {
            Vue.prototype.$message({
                type: 'success',
                message: '登录成功'
            })
            state.account = response.body['account']
            state.nickname = response.body['nickname']
            state.isTeacher = response.body['is_teacher']
            state.background_blur = false
            state.showLogin = false
            router.push('/roomList')
        },
        'GET_ROOMS_FAIL': function (state, err) {
            Vue.prototype.$message({
                message: '获取直播房间失败',
                type: 'error',
            })
        },
        'CHANGE_PASSWORD_SUCC': function (state, response) {
            Vue.prototype.$message({
                message: response.body.detail,
                type: 'success',
            })
            state.showInfo = false
            state.account = null
            state.nickname = null
            state.isTeacher = false
            router.push('/roomList')
        },
        /**
         *
         * @method trueBlur
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueBlur: function (state) {
            state.background_blur = true
        },
        /**
         *
         * @method falseBlur
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseBlur: function (state) {
            state.background_blur = false
        },
        /**
         *
         * @method trueRegister
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueRegister: function (state) {
            state.showRegister = true
        },
        /**
         *
         * @method falseRegister
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseRegister: function (state) {
            state.showRegister = false
        },
        /**
         *
         * @method trueLogin
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueLogin: function (state) {
            state.showLogin = true
        },
        /**
         *
         * @method falseLogin
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseLogin: function (state) {
            state.showLogin = false
        },
        /**
         *
         * @method trueForget
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueForget: function (state) {
            state.showForget = true
        },
        /**
         *
         * @method falseForget
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseForget: function (state) {
            state.showForget = false
        },
        /**
         *
         * @method trueCreateRoom
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueCreateRoom: function (state) {
            state.showCreateRoom = true
        },
        /**
         *
         * @method falseCreateRoom
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseCreateRoom: function (state) {
            state.showCreateRoom = false
        },
        /**
         * 获取登录用户信息
         *
         *
         * @method getUser
         * @param state {Object} An `state` Object
         * @param response {object} Get data object
         * @chainable
         */
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
        /**
         *
         * @method trueInfo
         * @param state {Object} An `state` Object
         * @chainable
         */
        trueInfo: function (state) {
            state.showInfo = true
        },
        /**
         *
         * @method falseInfo
         * @param state {Object} An `state` Object
         * @chainable
         */
        falseInfo: function (state) {
            state.showInfo = false
        },
        /**
         *
         * @method refreshNickname
         * @param state {Object} An `state` Object
         * @chainable
         */
        refreshNickname: function (state, nickname) {
            state.nickname = nickname
        },
        getHistory: function (state, response) {
            state.history = response.body
        },
        getHistoryFail: function (state) {
            Vue.prototype.$message({
                message: '获取录播房间失败',
                type: 'error',
            })
            // this.$message('fff') ???
        }
    },
    actions: {
        // We added a getRooms action for the initial load from the server
        // These URLs come straight from the Django URL router we did in Part 3
        /**
         * 获取房间到房间列表
         *
         *
         * @method getRooms
         * @param store {Object} An `store` Object
         * @return {Object} The liveroom
         */
        getRooms (store) {
            return api.get(apiRoot + '/liveroom/')
                .then((response) => store.commit('GET_ROOMS', response))
                .catch((error) => store.commit('GET_ROOMS_FAIL', error))
        },
        getHistory (state) {
            return api.get(apiRoot + '/history/')
                .then((response) => store.commit('getHistory', response))
                .catch((error) => store.commit('getHistoryFail', error))
        },
        addRoom (store, room) {
            return api.post(apiRoot + '/rooms/', room)
                .then((response) => store.commit('ADD_ROOM', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        clearRooms (store) {
            return api.delete(apiRoot + '/rooms/clear_rooms/')
                .then((response) => store.commit('CLEAR_ROOMS'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户登录的检测是否成功
         *
         *
         * @method loginUser
         * @param store {Object} An `store` Object
         * @param userinfo {Object} An `userinfo` Object
         * @return {Object} The result
         */
        loginUser (store, userinfo) {
            return api.post(apiRoot + '/users/login_users/', userinfo)
                .then((response) => store.commit('SUCC_LOGIN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户注册的检测是否成功
         *
         *
         * @method RegisterUser
         * @param store {Object} An `store` Object
         * @param userinfo {Object} An `userinfo` Object
         * @return {Object} The result
         */
        registerUser (store, userinfo) {
            return api.post(apiRoot + '/users/', userinfo)
                .then((response) => store.commit('Register_SUCC', userinfo))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户修改昵称，并且保存在后端
         *
         *
         * @method changeNick
         * @param store {Object} An `store` Object
         * @param userinfo {Object} An `userinfo` Object
         * @return {Object} The result
         */
        changeNick (store, userinfo) {
            userinfo.account = store.state.account
            return api.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => {
                    store.commit('API_SUCC', response)
                    store.commit('refreshNickname', userinfo.nickname)
                })
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户修改密码，检测是否成功，并且保存在后端
         *
         *
         * @method changePasswd
         * @param store {Object} An `store` Object
         * @param userinfo {Object} An `userinfo` Object
         * @return {Object} The result
         */
        changePasswd (store, userinfo) {
            return api.patch(apiRoot + '/users/change_info/', userinfo)
                .then((response) => store.commit('CHANGE_PASSWORD_SUCC', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户发送验证码
         *
         *
         * @method sendVertificateCode
         * @param store {Object} An `store` Object
         * @param vertificateInfo {Object} An `vertificateInfo` Object
         * @return {Object} The result
         */
        sendVertificateCode (store, vertificateInfo) {
            return api.post(apiRoot + '/users/sendVertificateCode/', vertificateInfo)
                .then((response) => store.commit('API_SUCC', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户忘记密码
         *
         *
         * @method forgetPassword
         * @param store {Object} An `store` Object
         * @param  info {Object} An ` info` Object
         * @return {Object} The result
         */
        forgetPassword (store, info) {
            return api.patch(apiRoot + '/users/forget_info/', info)
                .then((response) => store.commit('API_SUCC', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 用户成功登出
         *
         *
         * @method logout
         * @param store {Object} An `store` Object
         * @return {Object} The result
         */
        logout (store) {
            return api.post(apiRoot + '/users/logout_user/')
                .then((response) => store.commit('LOGOUT_SUCC'))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 打开注册窗口
         *
         *
         * @method openRegisterDialog
         */
        openRegisterDialog: function () {
            store.commit('trueRegister')
            store.commit('trueBlur')
        },
        /**
         * 关闭注册窗口
         *
         *
         * @method closeRegisterDialog
         */
        closeRegisterDialog: function () {
            store.commit('falseRegister')
            store.commit('falseBlur')
        },
        /**
         * 打开登录窗口
         *
         *
         * @method openLoginDialog
         */
        openLoginDialog: function () {
            store.commit('trueLogin')
            store.commit('trueBlur')
        },
        /**
         * 打开忘记密码窗口
         *
         *
         * @method openForgetDialog
         */
        openForgetDialog: function () {
            store.commit('trueForget')
            store.commit('trueBlur')
        },
        /**
         * 关闭忘记密码窗口
         *
         *
         * @method closeForgetDialog
         */
        closeForgetDialog: function () {
            store.commit('falseForget')
            store.commit('falseBlur')
        },
        /**
         * 关闭登录窗口
         *
         *
         * @method closeLoginDialog
         */
        closeLoginDialog: function () {
            store.commit('falseLogin')
            store.commit('falseBlur')
        },
        /**
         * 打开创建直播间窗口
         *
         *
         * @method openCreateRoomDialog
         */
        openCreateRoomDialog: function () {
            store.commit('trueCreateRoom')
            store.commit('trueBlur')
        },
        /**
         * 关闭创建直播间窗口
         *
         *
         * @method closeCreateRoomDialog
         */
        closeCreateRoomDialog: function () {
            store.commit('falseCreateRoom')
            store.commit('falseBlur')
        },
        /**
         * 获取用户从后端
         *
         *
         * @method getUserFromDjango
         * @return {Object} The result
         */
        getUserFromDjango: function () {
            return api.post(apiRoot + '/users/current_user/')
                .then((response) => store.commit('getUser', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        /**
         * 打开个人信息窗口
         *
         *
         * @method openInfoDialog
         */
        openInfoDialog: function () {
            store.commit('trueInfo')
            store.commit('trueBlur')
        },
        /**
         * 关闭个人信息窗口
         *
         *
         * @method closeInfoDialog
         */
        closeInfoDialog: function () {
            store.commit('falseInfo')
            store.commit('falseBlur')
        },
        startLive: function (store, roomInfo) {
            return api.patch(apiRoot + '/liveroom/start_live/', roomInfo)
                .then((response) => store.commit('API_SUCC', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        stopLive: function (store, roomInfo) {
            return api.patch(apiRoot + '/liveroom/stop_live/', roomInfo)
                .then((response) => store.commit('API_SUCC', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
    }
})

export default store
