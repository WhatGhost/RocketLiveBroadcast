<template>
    <div class="main-div shadow-fixed">
        <div class="above-div">
            <transition-group name="itemlist" tag="div">
                <chat-item v-for="msg in messageList" v-bind:message="msg" :key="index">
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
import io from '../../lib/socket.io'
import ChatItem from './ChatItem'

export default {
    components: {
        Chat,
        ChatItem
    },
    data: function () {
        return {
            num: 0,
            messageList: [],
            message: '',
            nickname: '',
            isTeacher: false,
            httpServer: null,
            roomId: this.$route.params['id'],
            showEmoji: false,
            emojis: ['😂', '🙏', '😄', '😏', '😇', '😅', '😌', '😘', '😍', '🤓', '😜', '😎', '😊', '😳', '🙄', '😱', '😒', '😔', '😷', '👿', '🤗', '😩', '😤', '😣', '😰', '😴', '😬', '😭', '👻', '👍', '✌️', '👉', '👀', '🐶', '🐷', '😹', '⚡️', '🔥', '🌈', '🍏', '⚽️', '❤️', '🇨🇳']
        }
    },
    computed: {
        index: function () {
            this.num += 1
            return this.num
        }
    },
    created() {
        this.nickname = this.$store.state.nickname
        this.isTeacher = this.$store.state.isTeacher
    },
    mounted() {
        this.connectEvent()
    },
    methods: {
        connectEvent() {
            this.httpServer = io.connect('http://127.0.0.1:3000')
            this.httpServer.emit('init', {
                roomId: this.roomId
            })
            this.httpServer.on('message', (obj) => {
                this.messageList.push(obj)
            })
        },
        sendMessage() {
            let messageToSend = {
                content: this.message,
                nickname: this.nickname,
                roomId: this.roomId,
                highlight: this.isTeacher
            }
            if (this.message !== '') {
                this.httpServer.emit('message', messageToSend)
                this.messageList.push(messageToSend)
                this.message = ''
            }
//            console.log(this.$store.state.nickname)
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
