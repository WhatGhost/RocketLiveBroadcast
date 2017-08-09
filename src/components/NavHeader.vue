<template>
    <div>
        <div class="whole-div" v-bind:class="{ blur: $store.state.background_blur }">
            <el-button type="text" id="open-room-btn" @click="showCreateRoom">开房</el-button>
            <el-button type="text"  @click="showRoomList">主页</el-button>
            <div id="blank"></div>
            <div id="right-btns">
                <el-button class="show-modal-btn" type="text"
                           @click="logout" v-if="this.logged">Log Out
                </el-button>
                <el-button class="show-modal-btn" type="text"
                           @click="showInfo" v-if="this.logged">{{userName}}
                </el-button>
                <el-button class="show-modal-btn" type="text"
                           @click="openRegisterDialog">Register
                </el-button>
                <el-button class="show-modal-btn" type="text"
                           @click="openLoginDialog">Log in
                </el-button>
            </div>
        </div>
        <register-modal-dialog></register-modal-dialog>
        <login-modal-dialog></login-modal-dialog>
    </div>
</template>

<script>
    import ElButton from '../../node_modules/element-ui/packages/button/src/button.vue'
    import RegisterModalDialog from './RegisterModalDialog.vue'
    import LoginModalDialog from './LoginModalDialog'

    export default {
        components: {
            ElButton,
            RegisterModalDialog,
            LoginModalDialog
        },
        data: function () {
            return {
                userName: 'leto',
                logged: true,
                isTeacher: false,
                isBlur: true
            }
        },
        methods: {
            switchBlur: function () {
                this.isBlur = !this.isBlur
            },
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
                this.$router.push('info')
            },
            showCreateRoom: function () {
                // this.$emit('goto', 'CreateRoom')
                this.$router.push('createRoom')
            },
            showRoomList: function () {
                this.$store.dispatch('getRooms')
                this.$router.push('roomList')
            },
            openRegisterDialog: function () {
                this.$store.dispatch('openRegisterDialog')
            },
            openLoginDialog: function () {
                this.$store.dispatch('openLoginDialog')
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
        background-color: #f7f7f7;
        color: white;
    }

    .show-modal-btn {
        font-size: 16px;
        color: #BCB8B8;
        margin-left: 0;
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
        background-color: #81cdc6;
        color: white;
    }
</style>

