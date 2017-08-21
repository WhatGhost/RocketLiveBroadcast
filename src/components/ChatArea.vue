<template>
    <div class="main-div shadow-fixed">
        <div class="above-div">
            <transition-group name="itemlist" tag="div">
                <chat-item @ban="ban" @kickout="kickout" v-for="(msg, key) in messageList" :message="msg" :isRoomCreator="userInfo.isRoomCreator" :key="key">
                </chat-item>
            </transition-group>
            <banned-list :bannedUsers="bannedUsers" :roomInfo="roomInfo" @unban="unban"></banned-list>
        </div>
        <div class="emoji-div" v-if="showEmoji">
        </div>
        <div class="bottom-bar">
            <el-button class="bottom">😄</el-button>
            <el-input class="mes-input bottom" v-model="message" autoComplete="" omplete="off"></el-input>
            <el-button class="bottom" @click='sendMessage'>send</el-button>
            <el-button class="bottom" @click='showBannedUsers' v-show="userInfo.isRoomCreator">showBannedUsers</el-button>
            <el-button class="bottom" @click='banAll' v-show="userInfo.isRoomCreator && !bannedStatus">banAll</el-button>
            <el-button class="bottom" @click='unbanAll' v-show="userInfo.isRoomCreator && bannedStatus">undo banAll</el-button>
        </div>
    </div>
</template>

<script>
import ChatItem from './ChatItem'
import BannedList from './BannedList'

export default {
    props: ['httpServer', 'roomInfo', 'userInfo'],
    components: {
        ChatItem,
        BannedList
    },
    data: function () {
        return {
            messageList: [],
            bannedUsers: [],
            bannedStatus: false, // 记录是否是全局禁言
            message: '',
            showEmoji: false,
            emojis: ['😂', '🙏', '😄', '😏', '😇', '😅', '😌', '😘', '😍', '🤓', '😜', '😎', '😊', '😳', '🙄', '😱', '😒', '😔', '😷', '👿', '🤗', '😩', '😤', '😣', '😰', '😴', '😬', '😭', '👻', '👍', '✌️', '👉', '👀', '🐶', '🐷', '😹', '⚡️', '🔥', '🌈', '🍏', '⚽️', '❤️', '🇨🇳']
        }
    },
    created() {
        this.httpServer.on('message', (obj) => {
            this.messageList.push(obj)
        })
        this.httpServer.on('getBannedList', (obj) => {
            this.bannedUsers = obj
        })
        this.httpServer.on('getBannedStatus', (obj) => {
            this.bannedStatus = obj
        })
    },
    methods: {
        sendMessage: function () {
            let messageToSend = {
                content: this.message,
                userInfo: this.userInfo,
                roomId: this.roomInfo.roomId,
                status: 200
            }
            if (this.message !== '') {
                this.httpServer.emit('message', messageToSend)
                this.message = ''
            }
        },
        ban: function (obj) {
            if (this.userInfo.isRoomCreator) {
                this.httpServer.emit('ban', obj)
            }
        },
        unban: function (obj) {
            if (this.userInfo.isRoomCreator) {
                this.httpServer.emit('unban', obj)
            }
        },
        kickout: function (obj) {
            if (this.userInfo.isRoomCreator) {
                this.httpServer.emit('kickout', obj)
            }
        },
        showBannedUsers: function () {
            this.httpServer.emit('getBannedList', {
                roomId: this.roomInfo.roomId
            })
        },
        banAll: function () {
            if (this.userInfo.isRoomCreator) {
                this.httpServer.emit('banAll', {
                    roomId: this.roomInfo.roomId
                })
            }
        },
        unbanAll: function () {
            if (this.userInfo.isRoomCreator) {
                this.httpServer.emit('unbanAll', {
                    roomId: this.roomInfo.roomId
                })
            }
        }
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.above-div {
    height: 78%;
    margin-top: 0;
    overflow-y: scroll;
    background-color: lightcyan;
}

.bottom-bar {
    display: flex;
    flex-direction: row;
    /*margin: 5px;*/
    /*height: 18%;*/
}

.mes-input {
    padding: 0 5px 0 5px;
}

.bottom {
    /*height: 100%;*/
}

.itemlist-enter-active,
.itemlist-leave-active {
    transition: all 1s;
}

.itemlist-enter,
.itemlist-leave-active {
    opacity: 0;
}
</style>
