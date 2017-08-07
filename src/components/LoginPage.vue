<template>
    <div class="login-div">
        <div>
            <h1>登录</h1>
            <p class="tip">账号</p>
            <el-input id="user-name" type="text" placeholder="电子邮箱或手机号码" v-model="userName"></el-input>
            <p class="tip">密码</p>
            <el-input id="user-password" type="password" placeholder="请输入密码" v-model="userPassword"></el-input>
            <el-button type="primary" class="sure-btn" @click="loginButtonClick">确认</el-button>
            <br/>
            <el-button type="text" class="forget-btn" @click="this.showForget">忘记密码</el-button>
        </div>
    </div>
</template>


<script>
    import ElInput from '../../node_modules/element-ui/packages/input/src/input.vue'

    export default {
        components: {ElInput},
        data: function () {
            return {
                userName: '',
                userPassword: ''
            }
        },
        methods: {
            loginButtonClick() {
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
                this.$store.dispatch('loginUser', {
                    account: this.account,
                    password: this.password
                })
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

    #user-password, #user-name {
        display: block;
    }

    .sure-btn {
        font-size: 20px;
        background-color: #00af50;
        border-radius: 20px;
        width: 384px;
        height: 40px;
        margin-top: 30px;
    }

    .forget-btn {
        font-size: 16px;
        margin-top: 20px;
    }

</style>
