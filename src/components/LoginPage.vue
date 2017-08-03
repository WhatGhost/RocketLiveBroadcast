<template>
    <div class="login-panel">
        <div>
            <label  >登录</label>
            <input id='user-name' type="text" placeholder="用户名" v-model="userName">
        </div>
        <div>
            <input id='user-password' type="text" placeholder="密码" v-model="userPassword" >
        </div>
        <button class='login-button' @click="loginButtonClick">确认</button>
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
        loginButtonClick() {
            if (this.userName === '') {
                window.alert('用户名不能为空')
                return
            }
            if (this.userPassword === '') {
                window.alert('密码不能为空')
            }
            console.log('Username:  ' + this.userName + '\n Password:  ' + this.userPassword)
        }
    }
}
</script>
<style scoped>
.login-panel {
    margin-top: 50px;
    margin-bottom: 30px;
}

.login-button {
    width: 100%;
    height: 50px;
    background-color: green;
    border-radius: 20px;
    color: #FFF;
    font-size: 30px;
}
label {
    margin-top: 30px;
    margin-bottom: 30px;
    display: block;
    font-size: 40px;
}
input {
    margin-top: 30px;
    margin-bottom: 30px;
    display: block;
    width: 100%;
    line-height: 50px;
    border-radius: 10px;
}
</style>
