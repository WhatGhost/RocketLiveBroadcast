<template>
    <div class="main-div">
        <div class="above-div">
            <div class="items">
                <chat-item v-for="msg in messageList" v-bind:message="msg">
                </chat-item>
            </div>
            <div class="emoji-div" v-if="showEmoji">
            </div>
        </div>
        <div class="bottom-bar">
            <el-button>😄</el-button>
            <el-input class="mes-input" v-model="message" autocomplete="off"></el-input>
            <el-button @click='sendMessage'>send</el-button>
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
    justify-content: flex-end;
}

.above-div {
    height: 80%;
    background-color: #fafafa;
}

.items {
    overflow-y: scroll;
    height: 95%;
}

.bottom-bar {
    display: flex;
    flex-direction: row;
    margin: 5px;
}

.mes-input {
    padding: 0 5px 0 5px;
}

</style>
