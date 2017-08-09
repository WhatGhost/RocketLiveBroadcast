<template>
    <div id="main-div">
        <div class="two-sides">
            <div id="tag">
                <el-button type="primary" id="personal-information" @click="switchLabel('personalInformation')">个人信息
                </el-button>
                <el-button type="primary" id="change-password" @click="switchLabel('changePassword')">修改密码</el-button>
                <el-button type="primary" id="change-nickname" @click="switchLabel('changeNickname')">修改昵称</el-button>
            </div>
        </div>
         <router-view></router-view>
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
        },
        methods: {
            switchLabel: function(destination) {
                this.$router.push('/info/' + destination)
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
