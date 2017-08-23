<template>
    <div class="main-div shadow-fixed">
        <div class="above-div" id="scrolled">
            <transition-group name="itemlist" tag="div">
                <chat-item @ban="ban"
                           @kickout="kickout"
                           v-for="(msg, key) in messageList"
                           :message="msg"
                           :showOpButton="isShowOptions"
                           :isRoomCreator="userInfo.isRoomCreator"
                           :key="key">
                </chat-item>
            </transition-group>
            <div v-if="isShowOptions" class="option-buttons">
                <el-button type="primary"
                           @click="banAll"
                           v-show="!bannedStatus">ban All
                </el-button>
                <el-button type="primary"
                           @click="unbanAll"
                           v-show="bannedStatus">unban All
                </el-button>
                <el-button type="primary"
                           @click="showBannedUsers">banned list
                </el-button>
            </div>
        </div>
        <div class="emoji-div" v-if="showEmoji">
        </div>
        <div class="bottom-bar">
            <el-button class="bottom">😄</el-button>
            <el-input class="mes-input"
                      ref="input"
                      v-model="message"
                      autoComplete=""
                      omplete="off"></el-input>
            <el-button @click='sendMessage'>send
            </el-button>
            <el-button type="primary"
                       :icon="optionIcon"
                       v-bind:class="{ orange:isShowOptions }"
                       @click="switchShowOptions"
                       v-show="userInfo.isRoomCreator">
            </el-button>
        </div>
        <banned-list :bannedUsers="bannedUsers"
                     v-if="showBannedList"
                     @closeBannedList="showBannedList=false"
                     :roomInfo="roomInfo"
                     @unban="unban"></banned-list>
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
            emojis: ['😂', '🙏', '😄', '😏', '😇', '😅', '😌', '😘', '😍', '🤓', '😜', '😎', '😊', '😳', '🙄', '😱', '😒', '😔', '😷', '👿', '🤗', '😩', '😤', '😣', '😰', '😴', '😬', '😭', '👻', '👍', '✌️', '👉', '👀', '🐶', '🐷', '😹', '⚡️', '🔥', '🌈', '🍏', '⚽️', '❤️', '🇨🇳'],
            isShowOptions: false,
            showBannedList: false
        }
    },
    created () {
        this.showBannedList = false
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
    mounted: function () {
        document.querySelector('.el-input__inner').style.height = '100%'
    },
    updated: function () {
        let objDiv = document.getElementById('scrolled')
        objDiv.scrollTop = objDiv.scrollHeight
    },
    computed: {
        optionIcon: function () {
            if (!this.isShowOptions) {
                return 'setting'
            } else {
                return 'close'
            }
        }
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
            this.showBannedList = true
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
        },
        switchShowOptions: function () {
            this.isShowOptions = !this.isShowOptions
        }
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.above-div {
    height: 82%;
    margin-top: 0;
    overflow-y: scroll;
    background-color: lightcyan;
}

.option-buttons {
    float: right;
}

.bottom-bar {
    display: flex;
    flex-direction: row;
    height: 17%;
    margin-bottom: 1%;
    min-height: 36px;
}

.mes-input {
    padding: 0 5px 0 5px;
    height: 100%;
    margin-top: auto;
    margin-bottom: auto;
}

.orange {
    border: orange;
    background-color: orange;
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
