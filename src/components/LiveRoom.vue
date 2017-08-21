<template>
    <div class="live-room" v-bind:class="{ blur: $store.state.background_blur }" id='elementToShare'>
        <div class="message">
            <p>房间人数： {{ userCount }}</p>
        </div>
        <div ref="recordArea" class="room">
            <button @click="createCanvas">CreateCanvas</button>
            <button id="start" @click="startRecord" contenteditable="false">Start Canvas Recording</button>
            <button id="stop" @click="stopRecord" disabled contenteditable="false">Stop</button>
            <div class='left shadow-fixed'>
                <div class="top-btn-div" :class="userInfo.isRoomCreator?'':'hiding'">
                    <el-button class="top-btn" @click="switchPane('pdfViewer')">PDF</el-button>
                    <el-button class="top-btn" @click="switchPane('codeEditor')">Code Editor</el-button>
                    <el-button class="top-btn" @click="switchPane('whiteBoard')">WhiteBoard</el-button>
                </div>
                <pdf-viewer :hide="hidePdfViewer" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></pdf-viewer>
                <code-editor-page :hide="hideCodeEditor" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></code-editor-page>
                <white-board-page :hide="hideWhiteBoard" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></white-board-page>
            </div>
            <div class='right'>
                <record-video class="video-area" :userInfo="userInfo" :roomInfo="roomInfo"></record-video>
                <chat-area class="chat-area" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></chat-area>
            </div>
        </div>
    </div>
</template>

<script>
import WhiteBoardPage from './WhiteboardPage'
import CodeEditorPage from './CodeEditorPage'
import RecordVideo from './RecordVideo'
import ChatArea from './ChatArea'
import PdfViewer from './PdfViewer'
import io from '../../lib/socket.io'

export default {
    components: {
        WhiteBoardPage,
        CodeEditorPage,
        RecordVideo,
        ChatArea,
        PdfViewer
    },
    data: function () {
        return {
            isRecordingStarted: false,
            isStoppedRecording: false,
            showMessageMenu: false,
            showingComponent: 'codeEditor',
            userCount: 0,
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
                isRoomCreator: false,
                account: ''
            },
            canvas2d: null,
            recorder: null,
            context: null,
            recordAudio: null,
            elementToShare: null
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
            return '房间人数' + this.usersCount
        }
    },
    created() {
        this.getRoomInfo()
        this.getUserInfo()
        this.connect()
    },
    beforeDestroy() {
        this.httpServer.disconnect()
    },
    methods: {
        createCanvas: function () {
            this.appendCanvas()
            this.recorder = new window.RecordRTC(this.canvas2d, {
                type: 'canvas'
            })
        },
        appendCanvas: function () {
            this.elementToShare = document.getElementById('elementToShare')
            this.canvas2d = document.createElement('canvas')
            this.context = this.canvas2d.getContext('2d')
            this.canvas2d.width = this.elementToShare.clientWidth
            this.canvas2d.height = this.elementToShare.clientHeight
            this.canvas2d.style.top = 0
            this.canvas2d.style.left = 0
            this.canvas2d.style.zIndex = -1
            this.canvas2d.style.display = 'none'
            let el = (document.body || document.documentElement)
            el.appendChild(this.canvas2d)
        },
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
        getUserInfo: function () {
            this.userInfo.nickname = this.$store.state.nickname
            this.userInfo.isTeacher = this.$store.state.isTeacher
            this.userInfo.isRoomCreator = (this.roomInfo.__roomTeacherAccount === this.$store.state.account)
            this.userInfo.account = this.$store.state.account
        },
        connect: function () {
            this.httpServer = io.connect('http://127.0.0.1:3000')
            this.httpServer.on('userCountChange', (count) => {
                this.userCount = count
            })
            this.httpServer.emit('init', {
                roomId: this.roomInfo.roomId,
                userInfo: this.userInfo
            })
            this.httpServer.on('switchPane', (obj) => {
                this.showingComponent = obj.showingComponent
            })
            this.httpServer.emit('getCurrentData', {
                roomId: this.roomInfo.roomId
            })
        },
        switchPane: function (pane) {
            this.showingComponent = pane
            this.httpServer.emit('switchPane', {
                roomId: this.roomInfo.roomId,
                showingComponent: this.showingComponent
            })
        },
        startRecord: function () {
            navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
                let audio = document.createElement('audio')
                audio.muted = true
                audio.volume = 0
                audio.src = window.URL.createObjectURL(stream)
                console.log(audio)
                this.recordAudio = new window.RecordRTC(stream, {
                    type: 'audio',
                    recorderType: window.StereoAudioRecorder
                })
                // this.isStoppedRecording = false
                // this.isStartedRecording = true
                // console.log(hereStoppedRecording)
                // console.log(hereStartedRecording)
                // this.recorder.startRecording()
                this.recordAudio.startRecording()
                document.getElementById('stop').disabled = false
            })
            document.getElementById('start').disabled = true
            this.isStoppedRecording = false
            this.isRecordingStarted = true
            this.recorder.startRecording()
            window.setTimeout(function () {
                let stopButton = document.getElementById('stop')
                stopButton.disabled = false
            }, 10)
            this.looper()
        },
        stopRecord: function () {
            this.disabled = true
            this.isStoppedRecording = true
            this.recordAudio.stopRecording(function () {
                window.invokeSaveAsDialog(this.getBlob(), 'filename.wav')
            })
            this.recorder.stopRecording(function () {
                window.invokeSaveAsDialog(this.getBlob(), 'filename.webm')
            })
            document.getElementById('start').disabled = false
        },
        looper: function () {
            if (!this.isRecordingStarted) {
                return window.setTimeout(this.looper, 500)
            }
            let that = this
            window.html2canvas(that.elementToShare, {
                grabMouse: true,
                onrendered: function (canvas) {
                    that.context.clearRect(0, 0, that.canvas2d.width, that.canvas2d.height)
                    that.context.drawImage(canvas, 0, 0, that.canvas2d.width, that.canvas2d.height)
                    if (that.isStoppedRecording) {
                        return
                    }
                    window.setTimeout(that.looper, 40)
                }
            })
        }
    }
}
</script>

<style scoped>
.live-room {
    display: flex;
    flex-direction: column;
    height: 100%;
    align-content: flex-start;
}

.room {
    top: 80px;
    flex-direction: column;
    padding: 10px;
    height: 100%;
}

.left {
    float: left;
    width: 48%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border-radius: 4px;
    border: 1px solid #e5e5e5;
    background-color: rgba(255, 255, 255, 0.2);
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
    height: 75%;
}

.video-area {
    height: 80%;
    border-radius: 3px;
    border: 1px solid #e5e5e5;
    background-color: lightseagreen;
}

.chat-area {
    height: 50%;
    margin-top: 1%;
    border-radius: 5px;
    border: 1px solid #e5e5e5;
    background-color: rgba(255, 255, 255, 0.2);
}

.message {
    text-align: left;
    height: 3%;
    font-size: 9px;
    color: #d9d9d9;
    padding-left: 8px;
    margin-top: -5px;
    white-space: nowrap;
}

.hiding {
    display: none;
}
</style>
