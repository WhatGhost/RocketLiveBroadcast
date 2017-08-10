<template>
    <div class="main-div">
        <ul>
            <li v-for="msg in messageList">
                {{ msg.nickname}}: {{ msg.content }}
            </li>
        </ul>
        <button @click='sendMessage'>send</button>
        <input id="m" v-model="message" autocomplete="off">
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
            nickname: 'xiaoming',
            httpServer: null
        }
    },
    mounted() {
        this.connectEvent()
    },
    methods: {
        connectEvent() {
            this.httpServer = io.connect('http://127.0.0.1:3000')
            this.httpServer.on('message', (obj) => {
                this.messageList.push(obj)
            })
        },
        sendMessage() {
            if (this.message !== '') {
                this.httpServer.emit('message', {content: this.message, nickname: this.nickname})
            }
            this.messageList.push({content: this.message, nickname: this.nickname})
            this.message = ''
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

</style>
