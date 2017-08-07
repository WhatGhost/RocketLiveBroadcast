<template>
    <div class="main">
        <div>
            <h1>找回密码</h1>
            <p class="tip">账号</p>
            <el-input type="text" placeholder="账号邮箱" v-model="account"></el-input>
            <p class="tip">验证码</p>
            <div class="vertificate">
                <el-input type="text" placeholder="验证码" v-model="vertificateCode" class="vertificate-input"></el-input>
                <el-button type="text" @click="send-vertificate-code" class="send-email-btn">发送验证码</el-button>
            </div>
            <p class="tip">新密码</p>
            <el-input type="password" placeholder="密码" v-model="password"></el-input>
            <p class="tip">重复密码</p>
            <el-input type="password" placeholder="确认密码" v-model="surePassword"></el-input>
            <el-button @click="changePassword" class="sure-btn">确认</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        data: function () {
            return {
                account: '',
                vertificateCode: '',
                password: '',
                surePassword: '',
            }
        },
        methods: {
            sendVertificateCode () {

            },
            isPassword () {
                let patrn = /^(\w){8,20}$/
                return patrn.test(this.password)
            },
            changePassword () {
                if (this.account === '') {
                    window.alert('未填写邮箱或手机号码')
                    return 0
                }
                if (this.vertificateCode === '') {
                    window.alert('未填写验证码')
                    return 0
                }
                if (!this.checkVertification()) {
                    window.alert('验证码错误')
                    return 0
                }
                if (!this.isPassword()) {
                    window.alert('密码格式错误，请使用8至16位的数字、字母和下划线的组合')
                    return 0
                }
                if (this.password !== this.surePassword) {
                    window.alert('两次密码不一致')
                    return 0
                }
                return 1
            },
            checkVertification () {
                // check vertification code
                return true
            }
        }
    }
</script>

<style scoped>
    .main {
        margin-left: auto;
        margin-right: auto;
        display: flex;
        justify-content: center;
        width: 380px;
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

    .vertificate {
        display: flex;
        width: 350px;
    }

    .vertificate-input {
        display: inline-block;
        width: 250px;
    }

    .send-email-btn {
        font-size: 14px;
        font-weight: bold;
        margin-left: 30px;
    }

    .sure-btn {
        font-size: 20px;
        background-color: #00af50;
        color: white;
        border-radius: 20px;
        width: 384px;
        height: 40px;
        margin-top: 26px;
    }
</style>
