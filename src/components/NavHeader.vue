<template>
    <div>
        <div class="whole-div" v-bind:class="{ blur: $store.state.background_blur }">
            <el-button type="text" id="open-room-btn" v-if="$store.state.isTeacher"
                       @click="showCreateRoom">开房
            </el-button>
            <el-button class="home-btn" type="text" @click="showRoomList">主页</el-button>
            <div id="blank"></div>
            <div id="right-btns">
                <el-button class="right-text-btn" type="text"
                           @click="logout" v-if="logged">Log Out
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="showInfoDialog" v-if="logged">{{userName}}
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="openRegisterDialog" v-if="!logged">Register
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="openLoginDialog" v-if="!logged">Log in
                </el-button>
            </div>
        </div>
        <register-modal-dialog></register-modal-dialog>
        <login-modal-dialog></login-modal-dialog>
        <info-modal-dialog></info-modal-dialog>
        <forget-modal-dialog></forget-modal-dialog>
    </div>
</template>

<script>
import RegisterModalDialog from './RegisterModalDialog.vue'
import LoginModalDialog from './LoginModalDialog'
import InfoModalDialog from './InfoModalDialog'
import ForgetModalDialog from './ForgetModalDialog'

export default {
    components: {
        RegisterModalDialog,
        LoginModalDialog,
        InfoModalDialog,
        ForgetModalDialog
    },
    data: function () {
        return {
            isTeacher: false,
            isBlur: true
        }
    },
    computed: {
        userName: function () {
            console.log(this.$store.state.nickname)
            return this.$store.state.nickname
        },
        logged: function () {
            return this.$store.state.account !== null
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
            this.$store.dispatch('logout')
        },
        showLogin: function () {
            this.$emit('goto', 'LoginPage')
        },
        showInfoDialog: function () {
            this.$store.dispatch('openInfoDialog')
        },
        showCreateRoom: function () {
            // this.$emit('goto', 'CreateRoom')
            this.$router.push('createRoom')
        },
        showRoomList: function () {
            this.$store.dispatch('getRooms')
            this.$router.push('/roomList')
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
    border: none;
    background-color: #172645;
    /*background: -webkit-linear-gradient(left, red , blue); !* Safari 5.1 - 6.0 *!*/
    /*background: -o-linear-gradient(right, red, blue); !* Opera 11.1 - 12.0 *!*/
    /*background: -moz-linear-gradient(right, red, blue); !* Firefox 3.6 - 15 *!*/
    /*background: linear-gradient(to bottom, #29323c , #485563); !* 标准的语法 *!*/
    position: fixed;
    width: 100%;
    z-index: 100;
}

.home-btn {
    color: white;
}

.right-text-btn {
    font-size: 16px;
    color: white;
    margin-left: 0;
}

button {
    margin: 8px;
    width: 80px;
}

#blank {
    flex-grow: 1;
}

#open-room-btn {
    background-color: #81cdc6;
    color: white;
}
</style>

