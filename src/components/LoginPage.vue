<template>
    <div class="login-div">
        <div>
            <h1>登录</h1>
            <p class="tip">账号</p>
            <input id="user-name" type="text" placeholder="电子邮箱或手机号码" v-model="userName">
            <p class="tip">密码</p>
            <input id="user-password" type="password" placeholder="请输入密码" v-model="userPassword">
            <button class="sure-btn" @click="loginButtonClick">确认</button>
            <br/>
            <button class="forget-btn" @click="this.showForget">忘记密码</button>
        </div>
    </div>
</template>


<script>
    export default {
        data: function () {
            return {
                userName: '',
                userPassword: ''
            }
        },
        methods: {
            loginButtonClick () {
                if (this.userName === '') {
                    window.alert('用户名不能为空')
                    return
                }
                if (this.userPassword === '') {
                    window.alert('密码不能为空')
                    return
                }
                this.tryLogin()
            },
            showForget: function () {
                this.$emit('goto', 'Forget')
            },
            tryLogin: function () {
                console.log({password: this.userPassword, account: this.userName})
                this.$store.dispatch('loginUser', {password: this.userPassword, account: this.userName})
            }
        }
    }
</script>
<style scoped>
    .login-div {
        display: flex;
        justify-content: center;
    }

    h1 {
        font-size: 24px;
        font-weight: normal;
    }

    .tip {
        font-size: 14px;
        margin-bottom: 5px;
        text-align: left;
        color: #2C2C2C;
        padding-left: 4px;
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

    .forget-btn {
        font-size: 16px;
        color: #999999;
        background-color: transparent;
        border: none;
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
