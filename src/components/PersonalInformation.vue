<template>
    <div id="content">
        <div class="line">
            <label id="nickname-label">用户昵称：</label>
            <label id="nickname-value">{{ userName }}</label>
        </div>
        <div class="line">
            <label id="e-mail-label">{{ accountType }}</label>
            <label id="e-mail-value">{{ userAccount }}</label>
        </div>
    </div>
</template>
<script>
    export default {
        computed: {
            userName: function () {
                return this.$store.state.nickname
            },
            userAccount: function () {
                return this.$store.state.account
            },
            accountType: function () {
                if (this.userAccount.includes('@')) {
                    return '邮箱：'
                }
                return '手机号码：'
            }
        }
    }
</script>

<style scoped>
    #content {
        display: flex;
        flex-direction: column;;
    }

    .line {
        text-align: left;;
    }
</style>
