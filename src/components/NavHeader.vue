<template>
    <div class="whole-div">
        <button @click="showCreateRoom">开房</button>
        <button id="homepage-btn" @click="showRoomList">平台首页</button>
        <div id="blank"></div>
        <div id="right-btns">
            <button @click="showLogin">登录</button>
            <button @click="showRegister">注册</button>
            <button @click="logout" v-if="this.logged">登出</button>
            <button @click="showInfo" v-if="this.logged">{{userName}}</button>
        </div>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                userName: '',
                logged: false,
                isTeacher: false
            }
        },
        methods: {
            showRegister: function () {
                this.$emit('goto', 'Register')
            },
            logout: function () {
                this.loged = false
            },
            showLogin: function () {
                this.$emit('goto', 'LoginPage')
            },
            showInfo: function () {
                this.$emit('goto', 'Info')
            },
            showCreateRoom: function () {
                this.$emit('goto', 'CreateRoom')
            },
            showRoomList: function () {
                this.$emit('goto', 'RoomList')
            }
        }
    }
</script>

<style scoped>
    .whole-div {
        display: flex;
        align-items: center;
        height: 60px;
        border: none;
        background-color: #92d050;
        color: white;
    }

    button {
        margin: 8px;
        height: 34px;
        width: 80px;
        background-color: #e1efd9;
        border: none;
        outline: none;
    }

    #homepage-btn {
        background-color: transparent;
        color: white;
        border: none;
        outline: none;
    }

    #blank {
        flex-grow: 1;
    }
</style>

