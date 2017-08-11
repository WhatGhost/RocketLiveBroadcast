<template>
    <div id="content">
        <div class="line">
            <label id="nickname-label">用户昵称</label>
            <label id="nickname-value">{{userName}}</label>
        </div>
        <div class="line">
            <label id="e-mail-label">用户邮箱</label>
            <label id="e-mail-value">{{userAccount}}</label>
        </div>
    </div>
</template>
<script>
export default {
    computed: {
        userName: function () {
            console.log(this.$store.state.nickname)
            return this.$store.state.nickname
        },
        userAccount: function () {
            console.log(this.$store.state.account)
            return this.$store.state.account
        }
    }
}
</script>

<style scoped>
#content {
    display: flex;
    flex-direction: column;
    margin: 40px;
}

.line {
    margin: 10px;
    display: flex;
}
</style>
