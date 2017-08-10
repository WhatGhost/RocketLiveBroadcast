<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="this.$store.state.showRegister">
                <div class="modal-wrapper">
                    <div class="container">
                        <img class="side-img" src="../assets/dialog-side-register.svg">
                        <div class="right-side">
                            <div class="header">
                                <p class="title">Sign up</p>
                                <el-button type="text" class="close-btn"
                                           @click="closeDialog">×
                                </el-button>
                            </div>
                            <div class="dialog-body">
                                <!--<el-tooltip placement="bottom">-->
                                <input type="text" placeholder="E-MAIL OR PHONE NUM"
                                       class="input account" v-model="account">
                                <!--</el-tooltip>-->
                                <input type="text" placeholder="NICKNAME"
                                       class="input name" v-model="nickname">
                                <input type="password" placeholder="PASSWORD"
                                       class="input password" v-model="password">
                                <input type="password" placeholder="CONFIRM PASSWORD"
                                       class="input sure-password" v-model="confirmPassword">
                                <div class="vertificate">
                                    <input type="text" placeholder="VERIFICATION CODE"
                                           class="vertificate-input input" v-model="vertificateCode">
                                    <el-button type="text" class="send-code-btn"
                                               @click="sendVertificateCode">send
                                    </el-button>
                                </div>
                                <el-button type="primary" class="sure-btn shadow-m"
                                           @click="registerBtnClick">SIGN UP
                                </el-button>
                                <el-button type="text" class="to-login"><U>I&rsquo;m already member</U>
                                </el-button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                account: '',
                nickname: '',
                password: '',
                confirmPassword: '',
                vertificateCode: '',
            }
        },
        methods: {
            closeDialog: function () {
                this.$store.dispatch('closeRegisterDialog')
                this.errorMes = ''
            },
            showErrorMes: function (mes) {
                this.$message({
                    message: mes,
                    type: 'warning'
                })
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
            registerBtnClick: function () {
                if (this.account === '') {
                    this.showErrorMes('请填写电子邮箱或手机号码')
                    return
                }
                if (!(this.isRightEmail() || this.isRightPhoneNum())) {
                    this.showErrorMes('不是有效的电子邮箱或手机号码')
                    return
                }
                if (this.nickname === '') {
                    this.showErrorMes('未填写昵称')
                    return
                }
                // todo: make sure password's format
                if (this.password !== this.confirmPassword) {
                    this.showErrorMes('两次密码不一致')
                    return
                }
                if (!this.isPassword()) {
                    this.showErrorMes('密码格式不正确，请使用8至16位的数字、字母和下划线组合')
                    return
                }
                if (this.vertificateCode === '') {
                    this.showErrorMes('请填写验证码')
                    return
                }
                console.log('got dispatch before')
                this.$store.dispatch('registerUser', {
                    account: this.account,
                    nickname: this.nickname,
                    is_student: true,
                    password: this.password,
                    vertificateCode: this.vertificateCode
                })
            },
            sendVertificateCode() {
                if (this.account === '' || this.nickname === '' || this.password === '' || this.confirmPassword === '') {
                    this.errorMes = '以上信息未完成输入'
                    return
                }
                console.log('send button')
                this.errorMes = 'sendVertificateCode click'
                this.$store.dispatch('sendVertificateCode', {
                    account: this.account,
                })
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

    .side-img {
        height: 460px;
    }

    .right-side {
        margin-top: 15px;
    }

    .header {
        margin-left: -60px;
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
        left: 110px;
        top: -14px;
    }

    .dialog-body {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
        margin-left: -6px;
    }

    .input {
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
        margin-top: 15px;
    }

    .vertificate {
        display: flex;
        justify-content: space-around;
    }

    .vertificate-input {
    }

    .send-code-btn {
        font-size: 18px;
        font-weight: bold;
        margin-top: -24px;
        margin-left: 15px;
        float: right;
    }

    .to-login {
        margin-top: 15px;
        font-weight: bold;
    }
</style>
