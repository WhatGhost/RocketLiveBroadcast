<template>
    <div class="main">
        <h1>注册</h1>
        <input type="text" placeholder="电子邮箱或手机号码" class="account" v-model="account">
        <input type="text" placeholder="昵称" class="name" v-model="nickname">
        <input type="password" placeholder="密码" class="password" v-model="password">
        <input type="password" placeholder="确认密码" class="sure-password" v-model="confirmPassword">
        <div class="vertificate">
            <input type="text" placeholder="验证码" class="vertificate-input" v-model="vertificateCode">
            <button class="send-email-btn" @click="sendVertificateCode">发送邮件，获取验证码</button>
        </div>
        <button type="button" class="sure-btn" @click="registerBtnClick">确认</button>
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
    computed: {

    },
    methods: {
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
                password: this.password
            })
        },
        sendVertificateCode() {
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
    margin-left: auto;
    margin-right: auto;
}

h1 {
    font-size: 24px;
    font-weight: normal;
}

input {
    display: block;
    font-size: 16px;
    border: 1px solid #e8e8e8;
    padding-left: 10px;
    width: 350px;
    height: 26px;
    margin: 5px;
    border-radius: 2px;
}

.vertificate {
    margin-left: auto;
    margin-right: auto;
}

.vertificate-input {
    display: inline-block;
    width: 150px;
}

.send-email-btn {
    font-size: 16px;
    color: #007acc;
    margin-right: auto;
}

.sure-btn {
    font-size: 20px;
    display: block;
    border: none;
    background-color: #00af50;
    color: white;
    border-radius: 10px;
    width: 350px;
    height: 40px;
    margin: 15px;
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
