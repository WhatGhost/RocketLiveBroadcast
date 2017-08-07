<template>
    <div class="whole-div">
        <el-button id="open-room-btn" @click="showCreateRoom">开房</el-button>
        <el-button type="text" id="homepage-btn" @click="showRoomList">平台首页</el-button>
        <div id="blank"></div>
        <div id="right-btns">
            <el-button @click="showLogin">登录</el-button>
            <el-button @click="showRegister">注册</el-button>
            <el-button @click="logout" v-if="this.logged">登出</el-button>
            <el-button @click="showInfo" v-if="this.logged">{{userName}}</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                userName: 'leto',
                logged: true,
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
        width: 80px;
    }

    #homepage-btn {
        color: #2C2C2C;
        font-weight: bold;
    }

    #blank {
        flex-grow: 1;
    }

    #open-room-btn {
        background-color: yellow;
    }
</style>

