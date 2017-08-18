<template>
    <div>
        <el-input type="text" id="old-password" placeholder="原始密码" v-model="oldpassword"></el-input>
        <el-input type="password" id="new-password" placeholder="新密码" v-model="newpassword1"></el-input>
        <el-input type="password" id="renew-password" placeholder="再次输入新密码" v-model="newpassword2"></el-input>
        <el-button id="change" @click='changepasswdClick'>确认修改</el-button>
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
            changepasswdClick() {
                if (this.newpassword1 !== this.newpassword2) {
                    this.$message.error('两次密码不一致')
                    return
                }
                if (this.newpassword1 === '') {
                    this.$message.error('请完成输入')
                    return
                }
                // console.log(new window.Hashes.SHA256().hex(this.password))
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
    .inputs > * {
        margin: 10px;
    }

    .inputs {
        width: 300px;
    }

    #change {
    }
</style>
