<template>
    <div id="content">
        <div id="nickname">
            <label id="nicknamelabel">用户昵称</label>
            <label id="nicknamevalue">leto</label>
        </div>
        <div id="e-mail">
            <label id="e-maillabel">用户邮箱</label>
            <label id="e-mailvalue">123456789@qq.com</label>
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

#nicknamelabel,
#e-maillabel {
    flex: 1 1 100px;
    text-align: left;
    line-height: 50px;
}

#nicknamevalue,
#e-mailvalue {
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