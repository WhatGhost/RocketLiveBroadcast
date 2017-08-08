<template>
    <div class="main">
        <div>
            <h1>注册</h1>
            <p class="tip">账号</p>
            <input type="text" placeholder="电子邮箱或手机号码" class="account" v-model="account">
            <p class="tip">昵称</p>
            <input type="text" placeholder="昵称" class="name" v-model="nickname">
            <p class="tip">密码</p>
            <input type="password" placeholder="密码" class="password" v-model="password">
            <p class="tip">确认密码</p>
            <input type="password" placeholder="确认密码" class="sure-password" v-model="confirmPassword">
            <p class="tip">验证码</p>
            <div class="vertificate">
                <input type="text" placeholder="验证码" class="vertificate-input" v-model="vertificateCode">
                <span class="blank"></span>
                <button class="send-email-btn" @click="sendVertificateCode">发送邮件，获取验证码</button>
            </div>
            <button type="button" class="sure-btn" @click="registerBtnClick">确认</button>
        </div>
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
                vertificateCode: ''
            }
        },
        computed: {},
        methods: {
            isRightPhoneNum () {
                let phone = this.account
                return /^1[3|4|5|7|8]\d{9}$/.test(phone)
            },
            isRightEmail () {
                let re = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
                return re.test(this.account)
            },
            isPassword () {
                let patrn = /^(\w){8,20}$/
                return patrn.test(this.password)
            },
            registerBtnClick: function () {
                if (this.email === '') {
                    window.alert('请填写电子邮箱或手机号码')
                    return
                }
                if (!(this.isRightEmail() || this.isRightPhoneNum())) {
                    window.alert('不是有效的电子邮箱或手机号码')
                    return
                }
                if (this.nickname === '') {
                    window.alert('未填写昵称')
                    return
                }
                // todo: make sure password's format
                if (this.password !== this.confirmPassword) {
                    window.alert('两次密码不一致')
                    return
                }
                if (!this.isPassword()) {
                    window.alert('密码格式不正确，请使用8至16位的数字、字母和下划线组合')
                    return
                }
                if (this.vertificateCode === '') {
                    window.alert('请填写验证码')
                }
                this.$store.dispatch('registerUser', {
                    account: this.account,
                    nickname: this.nickname,
                    is_student: true,
                    password: this.password,
                    vertificateCode: this.vertificateCode,
                })
            },
            sendVertificateCode () {
                if (this.account === '' || this.nickname === '' || this.password === '' || this.confirmPassword === '') {
                    window.alert('以上信息未完成输入')
                    return
                }
                window.alert('sendVertificateCode click')
                this.$store.dispatch('sendVertificateCode', {
                    account: this.account,
                })
            }
        }
    }
</script>


<style scoped>
    .main {
        display: flex;
        justify-content: center;
    }

    h1 {
        font-size: 24px;
        font-weight: normal;
    }

    input {
        display: block;
        font-size: 16px;
        border: 2px solid #e8e8e8;
        width: 380px;
        height: 34px;
        margin-bottom: 5px;
        border-radius: 6px;
        padding-left: 0.5em;
    }

    .tip {
        font-size: 14px;
        margin-bottom: 5px;
        text-align: left;
        color: #2C2C2C;
        padding-left: 4px;
    }

    .vertificate {
        display: flex;
        width: 350px;
    }

    .blank {
        flex-grow: 4;
    }

    .vertificate-input {
        display: inline-block;
        width: 150px;
    }

    .send-email-btn {
        font-size: 14px;
        font-weight: bold;
        color: #00af50;
        background-color: transparent;
        border: none;
    }

    .sure-btn {
        font-size: 20px;
        border: none;
        background-color: #00af50;
        color: white;
        border-radius: 20px;
        width: 384px;
        height: 40px;
        margin-top: 20px;
    }

    input, button {
        outline: none;
    }

    input::-webkit-input-placeholder {
        /* WebKit browsers */
        color: #e8e8e8;
    }

    input:-moz-placeholder {
        /* Mozilla Firefox 4 to 18 */
        color: #e8e8e8;
    }

    input::-moz-placeholder {
        /* Mozilla Firefox 19+ */
        color: #e8e8e8;
    }

    input:-ms-input-placeholder {
        /* Internet Explorer 10+ */
        color: #e8e8e8;
    }
</style>
