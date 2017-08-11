<template>
    <div class="main-div">
        <ul>
            <li v-for="msg in messageList" :class="isTeacher?'highlight':''">
                {{ msg.nickname}}: {{ msg.content }}
            </li>
        </ul>
        <button @click='sendMessage'>send</button>
        <input id="m" v-model="message" autocomplete="off" :placeholder="roomId">
    </div>
</template>

<script>
import Chat from './Chat'
import io from '../../lib/socket.io'

export default {
    components: {
        Chat
    },
    data: function () {
        return {
            messageList: [],
            message: '',
            nickname: 'Various Artist',
            isTeacher: false,
            httpServer: null,
            roomId: this.$route.params['id']
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
            console.log(this.$store.state.nickname)
        }
    }
}
</script>

<style scoped>
/* copied from socket-io guidance */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

li {
    text-align: left;
}

.highlight {
    color: red;
}
</style>
