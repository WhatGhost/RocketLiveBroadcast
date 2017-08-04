<template>
    <div id='title1'>
        <div id='tag'>
            <button id='pi' @click="conversion='PersonalInformation'">个人信息</button>
            <button id='mp' @click="conversion='ChangePassword'">修改密码</button>
            <button id='mn' @click="conversion='ChangeNickname'">修改昵称</button>
        </div>
        <div id='centerdiv'></div>
        <component :is='conversion'></component>
    </div>
</template>
<script>
import PersonalInformation from './PersonalInformation.vue'
import ChangePassword from './ChangePassword.vue'
import ChangeNickname from './ChangeNickname.vue'
export default {
    components: {
        PersonalInformation,
        ChangeNickname,
        ChangePassword,
    },
    data: function () {
        return {
            conversion: 'PersonalInformation'
        }
    }
}
</script>
<style scoped>
#title1 {
    height: 300px;
    width: 700px;
    border: 5px solid black;
}

#tag {
    position: absolute;
    top: 40px;
    padding-left: 20px;
    display: flex;
    flex-direction: column;

    width: 200px;
    height: 120px;
}

#pi {
    flex: 1 1 40px;
    border: 1px solid grey;
    text-align: center;
    line-height: 40px;
}

#mp {
    flex: 1 1 40px;
    border: 1px solid grey;
    text-align: center;
    line-height: 40px;
}

#mn {
    flex: 1 1 40px;
    border: 1px solid grey;
    text-align: center;
    line-height: 40px;
}


#centerdiv {
    float: left;
    width: 250px;
    border-right: 1px dashed black;
    padding-bottom: 300px;
    margin-bottom: -300px;
}
</style>