<template>
    <div class="main-div">
        <h1>输入昵称</h1>
        <input type="text" v-model="newnickname" autofocus>
        <el-button class="sure-btn shadow-m" @click="changeNickname">change nickname</el-button>
    </div>
</template>
<script>
export default {
    data: function () {
        return {
            newnickname: '',
            account: ''
        }
    },
    methods: {
        changeNickname () {
            this.newnickname = this.newnickname.trim()
            if (this.newnickname === '') {
                this.$message({
                    message: '昵称不能为空',
                    type: 'warning'
                })
                return
            }
            this.$store.dispatch('changeNick', {
                nickname: this.newnickname,
                account: this.account,
                is_password: false
            })
        }
    }
}
</script>
<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    height: 250px;
}

h1 {
    color: #888888;
    font-size: 24px;
    height: 35px;
    margin-top: -4px;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 13px;
    margin: 30px 20px 20px 20px;
    padding-left: 0.2em;
}

.sure-btn {
    color: #2a2a2a;
    font-size: 18px;
    background-color: #fafd4a;
    border-radius: 20px;
    width: 200px;
    margin-top: 26px;
}
</style>
