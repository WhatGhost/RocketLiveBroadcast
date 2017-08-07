<template>
    <div class="main">
        <p id="tip">用户昵称</p>
        <el-input name="key" type="text" id="key" value="Leto" size="30"/>
        <el-button type="primary" id="change" @click="changeBtnClick">确认修改</el-button>
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
    .main {
        margin: 40px;
    }

    #tip {
        text-align: left;
    }

    #key {
        width: 250px;
    }

    #change {
        width: 100px;
        background-color: #00af50;
    }
</style>
