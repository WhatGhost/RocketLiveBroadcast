<template>
    <div class="main-div">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="container">
                        <el-button class="close-button"
                                   @click="closeBannedList"
                                   type="text">×
                        </el-button>
                        <h1 class="no-banned"
                            v-show="bannedUsers.length === 0">暂无被禁言用户</h1>
                        <h1 class="unban-tip"
                            v-show="bannedUsers.length !== 0">点击解禁</h1>
                        <div class="scrollArea" v-if="bannedUsers.length !== 0">
                            <transition-group name="itemlist" tag="div">
                                <el-button v-for="(user, key) in bannedUsers"
                                           type="text"
                                           class="unban-button"
                                           :key="key"
                                           @click="unban(user)">
                                    {{ user.nickname }}
                                </el-button>
                            </transition-group>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
export default {
    components: {},
    props: [
        'roomInfo',
        'bannedUsers'
    ],
    data () {
        return {}
    },
    methods: {
        unban: function (user) {
            console.log('unban clicked')
            this.$emit('unban', {
                userInfo: user,
                roomId: this.roomInfo.roomId,
            })
        },
        closeBannedList: function () {
            this.$emit('closeBannedList')
        }
    }
}
</script>

<style scoped>
.main-div {
    padding: 0 2px 5px 5px;
    margin-bottom: 7px;
}

.container {
    width: 400px;
    height: 250px;
    border-radius: 5px;
    margin: auto;
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
}

.close-button {
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 20px;
}

.no-banned {
    text-align: center;
    color: lightseagreen;
}

.unban-tip {
    text-align: left;
    margin-left: 20px;
    color: #01a0e4;
    font-size: 18px;
}

.unban-button {
    font-size: 20px;
    margin-left: 20px;
}

.scrollArea {
    width: 95%;
    height: 180px;
    border-right: none;
    margin-left: auto;
    margin-right: auto;
    overflow-y: auto;
}
</style>
