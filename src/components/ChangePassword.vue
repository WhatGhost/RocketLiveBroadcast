<template>
    <div>
        <div>
            <input type="text" id="old-password" placeholder="原始密码" size="30" />
        </div>
        <div>
            <input type="text" id="new-password" placeholder="新密码" size="30" />
        </div>
        <div>
            <input type="text" id="renew-password" placeholder="再次输入新密码" size="30" />
        </div>
        <div>
            <button id="change" @click="changeBtnClick">确认修改</button>
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
#old-password,
#new-password,
#renew-password {
    margin-top: 20px;
    margin-left: 80px;
    width: 250px;
    height: 30px;
}

#change {
    position: absolute;
    width: 100px;
    height: 30px;
    margin-top: 50px;
    margin-left: 150px;
    color: white;
    background-color: green;
    border-radius: 10px;
    background: #a5cd4e;
    /* Old browsers */
    background: -moz-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* FF3.6+ */
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #a5cd4e), color-stop(100%, #6b8f1a));
    /* Chrome,Safari4+ */
    background: -webkit-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* Chrome10+,Safari5.1+ */
    background: -o-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* Opera 11.10+ */
    background: -ms-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* IE10+ */
    background: linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* W3C */
}
</style>