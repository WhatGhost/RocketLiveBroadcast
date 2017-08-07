<template>
    <div id="content">
        <div class="line">
            <label id="nickname-label">用户昵称　</label>
            <label id="nickname-value">leto</label>
        </div>
        <div class="line">
            <label id="e-mail-label">用户邮箱　</label>
            <label id="e-mail-value">123456789@qq.com</label>
        </div>
    </div>
</template>
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
