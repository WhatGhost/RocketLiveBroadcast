<template>
    <div id="content">
        <div id="nickname">
            <label id="nickname-label">用户昵称</label>
            <label id="nickname-value">leto</label>
        </div>
        <div id="e-mail">
            <label id="e-mail-label">用户邮箱</label>
            <label id="e-mail-value">123456789@qq.com</label>
        </div>
    </div>
</template>
<style scoped>
#content {
    position: absolute;
    top: 210px;
    padding-left: 300px;
    width: 400px;
    display: flex;
    flex-direction: column;
}

#nickname {
    flex: 1 1 50px;
    display: flex;
    flex-direction: row;
}

#nickname-label,
#e-mail-label {
    flex: 1 1 100px;
    text-align: left;
    line-height: 50px;
}

#nickname-value,
#e-mail-value {
    flex: 3 3 300px;
    text-align: left;
    line-height: 50px;
}

#e-mail {
    flex: 1 1 50px;
    display: flex;
    flex-direction: row;
}
</style>