<template>
    <div class="main-div shadow-fixed">
        <div class="above-div">
            <transition-group name="itemlist" tag="div">
                <chat-item v-for="(msg, key) in messageList" v-bind:message="msg" :key="key">
                </chat-item>
            </transition-group>
        </div>
        <div class="emoji-div" v-if="showEmoji">
        </div>
        <div class="bottom-bar">
            <el-button class="bottom">😄</el-button>
            <el-input class="mes-input bottom" v-model="message" autoComplete="" omplete="off"></el-input>
            <el-button class="bottom" @click='sendMessage'>send</el-button>
        </div>
    </div>
</template>

<script>
import Chat from './Chat'
import ChatItem from './ChatItem'

export default {
    props: ['httpServer', 'roomInfo', 'userInfo'],
    components: {
        Chat,
        ChatItem
    },
    data: function () {
        return {
            messageList: [],
            message: '',
            showEmoji: false,
            emojis: ['😂', '🙏', '😄', '😏', '😇', '😅', '😌', '😘', '😍', '🤓', '😜', '😎', '😊', '😳', '🙄', '😱', '😒', '😔', '😷', '👿', '🤗', '😩', '😤', '😣', '😰', '😴', '😬', '😭', '👻', '👍', '✌️', '👉', '👀', '🐶', '🐷', '😹', '⚡️', '🔥', '🌈', '🍏', '⚽️', '❤️', '🇨🇳']
        }
    },
    created() {
        this.httpServer.on('message', (obj) => {
            this.messageList.push(obj)
        })
    },
    methods: {
        sendMessage() {
            let messageToSend = {
                content: this.message,
                nickname: this.userInfo.nickname,
                roomId: this.roomInfo.roomId,
                highlight: this.userInfo.isRoomCreator
            }
            if (this.message !== '') {
                this.httpServer.emit('message', messageToSend)
                this.messageList.push(messageToSend)
                this.message = ''
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
