<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="this.$store.state.showLogin">
                <div class="modal-wrapper">
                    <div class="container">
                        <div class="left-side">
                            <div class="header">
                                <p class="title">Log In</p>
                                <el-button type="text" class="close-btn"
                                           @click="closeDialog">×
                                </el-button>
                            </div>
                            <div class="dialog-body">
                                <input type="text" placeholder="E-MAIL OR PHONE NUM"
                                       v-model="account">
                                <input type="password" placeholder="PASSWORD"
                                       v-model="password">
                                <el-button type="primary" class="sure-btn shadow-m" @click="loginButtonClick">Log In
                                </el-button>
                                <br/>
                                <el-button type="text" class="to-forget" @click="this.showForget">
                                    <U>forget password</U></el-button>
                            </div>
                        </div>
                        <img class="side-img" src="../assets/dialog-side-login.svg">
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import Forget from './Forget'

export default {
    components: {
        Forget,
    },
    data: function () {
        return {
            account: '',
            password: ''
        }
    },
    methods: {
        closeDialog: function () {
            this.$store.dispatch('closeLoginDialog')
            this.errorMes = ''
        },
        showErrorMes: function (mes) {
            this.$message({
                message: mes,
                type: 'warning'
            })
        },
        loginButtonClick: function () {
            if (this.account === '') {
                this.showErrorMes('请填写电子邮箱或手机号码')
                return
            }
            // console.log(new window.Hashes.SHA256().hex(this.password))
            this.$store.dispatch('loginUser', {
                account: this.account,
                password: new window.Hashes.SHA256().hex(this.password)
            })
        },
        showForget: function () {
            this.$store.dispatch('closeLoginDialog')
            this.$store.dispatch('openForgetDialog')
        }
    }
}
</script>

<style scoped>
.container {
    width: 480px;
    height: 460px;
    margin: 0 auto;
    background-color: #fff;
    border-radius: 20px;
    box-shadow: 0 12px 25px -6px rgba(0, 0, 0, .35);
    transition: all .3s ease;
    display: flex;
}

.left-side {
    margin-top: 15px;
}

.header {
    color: #42b983;
    display: flex;
    justify-content: space-around;
}

.title {
    font-size: 20px;
    text-align: left;
    color: #808080;
}

.close-btn {
    color: #cacaca;
    font-size: 30px;
    position: relative;
    left: 70px;
    top: -14px;
}

.dialog-body {
    display: flex;
    flex-direction: column;
    margin-top: 70px;
    margin-left: 60px;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 13px;
    margin-bottom: 20px;
    padding-bottom: 8px;
    padding-left: 0.2em;
}

.sure-btn {
    font-size: 20px;
    background-color: #FF8C85;
    border-radius: 20px;
    margin-top: 25px;
}

.to-forget {
    margin-top: 15px;
    font-weight: bold;
}

.side-img {
    height: 460px;
    margin-left: auto;
    margin-right: -1px;
}
</style>
