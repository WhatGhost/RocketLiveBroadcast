<template>
    <div>
        <div id="title2">用户昵称</div>
        <el-input name="key" type="text" id="key" value="Leto" size="30" v-model="newnickname"></el-input>
        <el-button id="change" @click="changeNickname">确认修改</el-button>
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
            changeNickname() {
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
    .main {
        margin: 40px;
    }

    #tip {
        text-align: left;
    }

    #change {
    }
</style>
