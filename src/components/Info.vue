<template>
    <div id="main-div">
        <div class="two-sides">
            <div id="tag">
                <el-button type="primary" id="personal-information" @click="conversion='PersonalInformation'">个人信息
                </el-button>
                <el-button type="primary" id="change-password" @click="conversion='ChangePassword'">修改密码</el-button>
                <el-button type="primary" id="change-nickname" @click="conversion='ChangeNickname'">修改昵称</el-button>
            </div>
        </div>
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
    #main-div {
        display: flex;
        justify-content: center;
    }

    .two-sides {
        display: flex;
        flex-direction: row;
    }

    #tag {
        display: flex;
        flex-direction: column;
        width: 200px;
    }

    #tag > * {
        margin: 5px 20px;

    }

</style>
