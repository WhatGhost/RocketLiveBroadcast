<template>
    <div class="main-div">
        <div class="line1">
            <label id="nickname-label">用户昵称：</label>
            <label id="nickname-value">{{ userName }}</label>
        </div>
        <div class="line2">
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
                return '用户邮箱：'
            }
            return '手机号码：'
        }
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 200px;
}

.line1 {
    text-align: left;
    word-wrap: break-word;
    word-break: normal;
    margin-bottom: 10px;
    position: relative;
    top: -20px;
    left: 20px;
}

.line2 {
    text-align: left;
    position: relative;
    top: -20px;
    left: 20px;
    word-wrap: break-word;
    word-break: normal;
}

label {
    font-size: 17px;
    color: #4f4f4f;
}
</style>
