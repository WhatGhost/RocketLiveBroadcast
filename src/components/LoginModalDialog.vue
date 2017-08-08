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
    import ElButton from '../../node_modules/element-ui/packages/button/src/button.vue'

    export default {
        components: {ElButton},
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
            sendVerificationCode: function () {
            },
            isRightPhoneNum() {
                let phone = this.account
                return /^1[3|4|5|7|8]\d{9}$/.test(phone)
            },
            isRightEmail() {
                let re = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
                return re.test(this.account)
            },
            isPassword() {
                let patrn = /^(\w){8,20}$/
                return patrn.test(this.password)
            },
            loginButtonClick: function () {
                if (this.account === '') {
                    this.showErrorMes('请填写电子邮箱或手机号码')
                    return
                }
                if (!(this.isRightEmail() || this.isRightPhoneNum())) {
                    this.errorMes = '不是有效的电子邮箱或手机号码'
                    return
                }
                if (!this.isPassword()) {
                    this.errorMes = '密码格式不正确，请使用8至16位的数字、字母和下划线组合'
                    return
                }
                this.$store.dispatch('loginUser', {
                    account: this.account,
                    password: this.password
                })
            },
            showForget: function () {
            }
        }
    }
</script>

<style scoped>
    .alert {
        width: 500px;
        margin: 20px auto 0 auto;
        border-radius: 10px;
        transition: opacity .4s ease;
    }

    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .5);
        display: table;
        transition: opacity .3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }

    .modal-enter {
        opacity: 0;
    }

    .modal-leave-active {
        opacity: 0;
    }

    .modal-enter .container,
    .modal-leave-active .container {
        -webkit-transform: scale(1.1);
        transform: scale(1.1);
    }

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
        background-color: #00af50;
        border-radius: 20px;
        margin-top: 25px;
    }

    .to-forget {
        margin-top: 15px;
        font-weight: bold;
    }

    .side-img {
        height: 460px;
        position: relative;
        left: 32px;
    }

</style>
