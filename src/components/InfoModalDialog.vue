<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="this.$store.state.showInfo">
                <div class="modal-wrapper">
                    <div class="container">
                        <el-tabs type="card" class="info-tab">
                            <el-tab-pane label="个人信息">
                                <personal-information class="inner"></personal-information>
                            </el-tab-pane>
                            <el-tab-pane label="修改密码">
                                <change-password class="inner"></change-password>
                            </el-tab-pane>
                            <el-tab-pane label="修改昵称">
                                <change-nickname class="inner"></change-nickname>
                            </el-tab-pane>
                        </el-tabs>
                        <el-button class="close-btn" type="text" @click="closeDialog">×</el-button>
                        <!--<img class="image" src="../assets/info-image2.svg"/>-->
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import PersonalInformation from './PersonalInformation'
import ChangeNickname from './ChangeNickname'
import ChangePassword from './ChangePassword'

export default {
    components: {
        PersonalInformation,
        ChangeNickname,
        ChangePassword
    },
    data: function () {
        return {
            account: '',
            nickname: '',
            password: '',
            confirmPassword: '',
            vertificateCode: '',
        }
    },
    methods: {
        closeDialog: function () {
            this.$store.dispatch('closeInfoDialog')
            this.errorMes = ''
        },
        showErrorMes: function (mes) {
            this.$message({
                message: mes,
                type: 'warning'
            })
        }
    }
}
</script>

<style scoped>
.container {
    width: 460px;
    height: 260px;
    margin: 0 auto;
    background: #fff;
    border-radius: 14px;
    box-shadow: 0 12px 25px -6px rgba(0, 0, 0, .35);
    transition: all .3s ease;
    display: flex;
    justify-content: center;
    position: relative;
}

.close-btn {
    color: #cacaca;
    font-size: 30px;
    position: absolute;
    left: 425px;
    top: 10px;
}

.info-tab {
    width: 360px;
}

el-tab-pane {
    display: flex;
    justify-content: center;
}

.inner {
}

.image {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 460px;
}
</style>
