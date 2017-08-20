<template>
    <div class="main-div">
        <input type="text" placeholder="原始密码" v-model="oldpassword" autofocus>
        <input type="password" placeholder="新密码" v-model="newpassword1">
        <input type="password" placeholder="再次输入新密码" v-model="newpassword2">
        <el-button class="sure-btn shadow-m" @click='changepasswdClick'>change password</el-button>
    </div>
</template>
<script>
export default {
    data: function () {
        return {
            useraccount: '',
            oldpassword: '',
            newpassword1: '',
            newpassword2: ''
        }
    },
    computed: {},
    methods: {
        changepasswdClick () {
            if (this.newpassword1 !== this.newpassword2) {
                this.$message.error('两次密码不一致')
                return
            }
            if (this.newpassword1 === '') {
                this.$message.error('请完成输入')
                return
            }
            this.useraccount = this.$store.state.account
            this.$store.dispatch('changePasswd', {
                oldpassword: new window.Hashes.SHA256().hex(this.oldpassword),
                newpassword: new window.Hashes.SHA256().hex(this.newpassword1),
                account: this.useraccount,
                is_password: true
            })
        }
    },
}
</script>
<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    height: 250px;
    margin-top: 10px;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 13px;
    margin: 0 20px 25px 10px;
    padding-left: 0.2em;
}

.sure-btn {
    color: #2a2a2a;
    font-size: 18px;
    background-color: #fafd4a;
    border-radius: 20px;
    width: 200px;
}
</style>
