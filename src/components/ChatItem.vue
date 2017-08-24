<template>
    <div class="main-div">
        <div class="message-div"
             v-bind:class="{ highlight: message.userInfo.isRoomCreator, system: message.status === 403 }">
            <div class="header">
                <label class="name">{{ message.userInfo.nickname }}</label>
                <label class="currentTime">{{ currentTime }}</label>
            </div>
            <span class="mes-body shadow-fixed">{{ message.content }}</span>
            <div
                v-if="isRoomCreator && !message.userInfo.isRoomCreator && message.status !== 403 && showOpButton">
                <el-button type="text" class="ban-button" @click="ban">ban</el-button>
                <el-button type="text" class="out-button" @click="kickout">kickout</el-button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'message',
        'isRoomCreator',
        'showOpButton'
    ],
    data () {
        return {}
    },
    computed: {
        currentTime: function () {
            return new Date().toLocaleString()
        }
    },
    methods: {
        ban: function () {
            if (this.message.status === 200) {
                this.$emit('ban', this.message)
            }
        },
        kickout: function () {
            if (this.message.status === 200) {
                this.$emit('kickout', this.message)
            }
        }
    }
}
</script>

<style scoped>
.main-div {
    padding: 0 2px 5px 5px;
    margin-bottom: 7px;
}

.currentTime {
    font-size: 6px;
    color: #d9d9d9;
    text-align: right;
    float: right;
}

.mes-body {
    background-color: white;
    border-radius: 5px;
    padding: 2px 3px 2px 4px;
    margin-right: auto;
    font-size: 12px;
    margin-top: -2px;
}

.highlight span {
    background-color: yellow;
}

.system .name {
    color: #253b76;
}

.system span {
    color: white;
    background-color: #01a0e4;
}

.name {
    font-size: 8px;
}

.ban-button {
    background-color: #f9c855;
    border: none;
    padding: 3px;
    color: white;
}

.out-button {
    background-color: red;
    border: none;
    padding: 3px;
    color: white;
}
</style>
