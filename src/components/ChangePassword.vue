<template>
    <div>
        <div class="inputs">
            <el-input type="password" id="old-password" placeholder="原始密码" size="30"/>
            <el-input type="password" id="new-password" placeholder="新密码" size="30"/>
            <el-input type="password" id="renew-password" placeholder="再次输入新密码" size="30"/>
        </div>
        <div class="sure-div">
            <el-button type="primary" id="change" @click="changeBtnClick">确认修改</el-button>
        </div>
    </div>
</template>
<script>
    export default {
        methods: {
            changeBtnClick: function () {
                window.alert('创建成功')
            }
        }
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
        width: 100px;
        background-color: #00af50;
        margin: 10px;
    }

    .sure-div {
        display: flex;
        align-items: flex-end;
    }
</style>
