<template>
    <div class="live-room" v-bind:class="{ blur: $store.state.background_blur }">
        <div class="message">
            <p>{{ roomMessage }}</p>
        </div>
        <div class="room">
            <div class='left'>
                <div class="top-btn-div">
                    <el-button class="top-btn" @click="showingComponent = 'pdfViewer'">PDF</el-button>
                    <el-button class="top-btn" @click="showingComponent = 'codeEditor'">Code Editor</el-button>
                    <el-button class="top-btn" @click="showingComponent = 'whiteBoard'">WhiteBoard</el-button>
                </div>
                <pdf-viewer :hide="hidePdfViewer" :roomInfo="roomInfo" :httpServer="httpServer"></pdf-viewer>
                <code-editor-page :hide="hideCodeEditor"></code-editor-page>
                <white-board-page :hide="hideWhiteBoard"></white-board-page>
            </div>
            <div class='right'>
                <record-video class="video-area"></record-video>
                <chat-area class="chat-area"></chat-area>
            </div>
        </div>
    </div>
</template>

<script>
import LiveRoomMenu from './LiveRoomMenu'
import SlidePage from './SlidePage'
import WhiteBoardPage from './WhiteboardPage'
import CodeEditorPage from './CodeEditorPage'
import RecordVideo from './RecordVideo'
import ChatArea from './ChatArea'
import PdfViewer from './PdfViewer'
import io from '../../lib/socket.io'

export default {
    components: {
        LiveRoomMenu,
        SlidePage,
        WhiteBoardPage,
        CodeEditorPage,
        RecordVideo,
        ChatArea,
        PdfViewer
    },
    data: function () {
        return {
            showMessageMenu: false,
            showingComponent: 'pdfViewer',
            roomInfo: {
                roomId: -1,
                roomName: '',
                roomTeacher: '',
                roomIntroduction: '',
                // 没有必要请不要访问这个变量
                __roomTeacherAccount: ''
            },
            httpServer: null,
            userInfo: {
                nickname: '',
                isTeacher: false,
                isRoomCreator: false
            }
        }
    },
    computed: {
        hidePdfViewer: function () {
            return this.showingComponent !== 'pdfViewer'
        },
        hideCodeEditor: function () {
            return this.showingComponent !== 'codeEditor'
        },
        hideWhiteBoard: function () {
            return this.showingComponent !== 'whiteBoard'
        },
        roomMessage: function () {
            return '房间名：如何构建单页面应用　　房间号：10010　　主讲教师：诸葛亮'
        }
    },
    created() {
        this.getRoomInfo()
        this.getUserInfo()
        this.connect()
    },
    methods: {
        switchMessageMenu: function () {
            this.showMessageMenu = !this.showMessageMenu
        },
        goHomepage: function () {
            // add vue rooter
        },
        getRoomInfo: function () {
            for (let i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.rooms[i].id === parseInt(this.$route.params['id'])) {
                    this.roomInfo.roomIntroduction = this.$store.state.rooms[i].room_introduction
                    this.roomInfo.roomTeacher = this.$store.state.rooms[i].room_creater.nickname
                    this.roomInfo.roomName = this.$store.state.rooms[i].room_name
                    this.roomInfo.__roomTeacherAccount = this.$store.state.rooms[i].room_creater.account
                }
            }
            this.roomInfo.roomId = this.$route.params['id']
        },
        getUserInfo: function() {
            this.userInfo.nickname = this.$store.state.nickname
            this.isTeacher = this.$store.state.isTeacher
            this.isRoomCreator = (this.roomInfo.__roomTeacherAccount === this.$store.state.account)
        },
        connect: function () {
            this.httpServer = io.connect('http://127.0.0.1:3000')
            this.httpServer.emit('init', {
                roomId: this.roomInfo.roomId
            })
            console.log('main connected')
        }
    }
}
</script>

<style scoped>
.live-room {
    display: flex;
    flex-direction: column;
}

.room {
    top: 80px;
    flex-direction: column;
    padding: 10px;
}

.left {
    float: left;
    width: 48%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-radius: 5px;
    border: 1px solid #e5e5e5;
}

.top-btn-div {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}

.top-btn {
    margin: 2px;
    font-size: 10px;
    padding: 6px;
    color: #888888;
}

.right {
    width: 50%;
    float: right;
    height: 400px;
}

.video-area {
    height: 80%;
    border-radius: 5px;
    border: 1px solid #e5e5e5;
}

.chat-area {
    height: 50%;
    margin-top: 10px;
    border-radius: 5px;
    border: 1px solid #e5e5e5;
}

.message {
    text-align: left;
    height: 24px;
    font-size: 9px;
    color: #d9d9d9;
    padding-left: 8px;
    margin-top: -5px;
    white-space: nowrap;
}
</style>
