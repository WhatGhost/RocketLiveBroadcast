<template>
    <div class="live-room" v-bind:class="{ blur: $store.state.background_blur }" id='elementToShare'>
        <div class="message">
            <p>房间人数： {{ userCount }}</p>
        </div>
        <div ref="recordArea" class="room">
            <div class="outer-left">
                <div class="buttons">
                    <el-button @click="createCanvas" class="hiding">Create Canvas</el-button>
                    <el-button id="start" @click="startRecord" contenteditable="false" class='hiding'>Start Recording
                    </el-button>
                    <el-button id="stop" @click="stopRecord" disabled contenteditable="false" class='hiding'>Stop</el-button>
                    <el-button @click="startLive" v-if="userInfo.isRoomCreator" v-show="!isRecordingStarted && !isStoppedRecording" id="startBtn">开始直播</el-button>
                    <el-button @click="stopLive" v-if="userInfo.isRoomCreator" v-show="!isStoppedRecording && isRecordingStarted" id="stopBtn">停止直播</el-button>
                    <!-- <el-button @click="startLive" v-if="userInfo.isRoomCreator" id="startBtn">开始直播</el-button>
                    <el-button @click="stopLive" v-if="userInfo.isRoomCreator" id="stopBtn">停止直播</el-button> -->
                    <el-button @click="controlEduArea" v-if="userInfo.isRoomCreator">教学区域</el-button>
                    <el-button @click="controlVideoArea" v-if="userInfo.isRoomCreator">视频区域</el-button>
                    <el-button @click="openCamera" v-if="userInfo.isRoomCreator && !isCameraOn">打开摄像头</el-button>
                    <!-- <el-button @click="closeCamera" v-if="userInfo.isRoomCreator && isCameraOn">关闭摄像头</el-button> -->
                    <el-button @click="openVideo" v-if="! userInfo.isRoomCreator" id='join'>打开视频</el-button>
                    <el-button @click="closeVideo" v-if="! userInfo.isRoomCreator" id='leave'>关闭视频</el-button>
                </div>
                <div class='left shadow-fixed' v-show="eduArea">
                    <div class="top-btn-div" :class="userInfo.isRoomCreator?'':'hiding'">
                        <el-button class="top-btn" @click="switchPane('pdfViewer')">Slide</el-button>
                        <el-button class="top-btn" @click="switchPane('codeEditor')">Code Editor</el-button>
                        <el-button class="top-btn" @click="switchPane('whiteBoard')">WhiteBoard</el-button>
                    </div>
                    <pdf-viewer :hide="hidePdfViewer" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></pdf-viewer>
                    <code-editor-page :hide="hideCodeEditor" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></code-editor-page>
                    <white-board-page :hide="hideWhiteBoard" :roomInfo="roomInfo" :httpServer="httpServer" :userInfo="userInfo"></white-board-page>
                </div>
            </div>
            <div class='right'>
                <record-video ref="recordVideo" class="video-area" :userInfo="userInfo" :roomInfo="roomInfo" v-show="videoArea"></record-video>
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
        PdfViewer,
    },
    data: function() {
        return {
            eduArea: true,
            videoArea: true,
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
            elementToShare: null,
            audioStream: null,
            canvasStream: null,
            isCameraOn: false,
            screenStream: null
        }
    },
    computed: {
        hidePdfViewer: function() {
            return this.showingComponent !== 'pdfViewer'
        },
        hideCodeEditor: function() {
            return this.showingComponent !== 'codeEditor'
        },
        hideWhiteBoard: function() {
            return this.showingComponent !== 'whiteBoard'
        },
        roomMessage: function() {
            return '房间人数' + this.usersCount
        }
    },
    created() {
        this.getRoomInfo()
        this.getUserInfo()
        this.connect()
        window.navigator.getUserMedia = window.navigator.getUserMedia || window.navigator.mozGetUserMedia || window.navigator.webkitGetUserMedia
    },
    beforeDestroy() {
        if (this.isRecordingStarted) {
            this.stopLive()
        } else {
            this.httpServer.disconnect()
        }
    },
    methods: {
        leave: function() {
            this.httpServer.disconnect()
        },
        controlEduArea: function() {
            if (this.eduArea === false) {
                this.eduArea = true
            } else {
                if (this.videoArea === true) {
                    this.eduArea = false
                }
            }
        },
        controlVideoArea: function() {
            if (this.videoArea === false) {
                this.$refs.recordVideo.publish()
                this.videoArea = true
            } else {
                if (this.eduArea === true) {
                    this.$refs.recordVideo.unpublish()
                    this.videoArea = false
                }
            }
        },
        captureScreen: function(cb) {
            window.getScreenId(function(error, sourceId, screenConstraints) {
                window.navigator.getUserMedia(screenConstraints, cb, function(error) {
                    console.error('getScreenId error', error)
                    window.alert('Failed to capture your screen. Please check Chrome console logs for further information.')
                })
            })
        },
        captureAudio: function(cb) {
            window.navigator.getUserMedia({ audio: true }, cb, function(error) { })
        },
        showErrorMes: function(mes) {
            this.$message({
                message: mes,
                type: 'error'
            })
        },
        switchMessageMenu: function() {
            this.showMessageMenu = !this.showMessageMenu
        },
        goHomepage: function() {
            // add vue rooter
        },
        getRoomInfo: function() {
            for (let i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.rooms[i].id === parseInt(this.$route.params['id'])) {
                    this.roomInfo.roomIntroduction = this.$store.state.rooms[i].room_introduction
                    this.roomInfo.roomTeacher = this.$store.state.rooms[i].room_creator.nickname
                    this.roomInfo.roomName = this.$store.state.rooms[i].room_name
                    this.roomInfo.__roomTeacherAccount = this.$store.state.rooms[i].room_creator.account
                }
            }
            this.roomInfo.roomId = this.$route.params['id']
        },
        getUserInfo: function() {
            this.userInfo.nickname = this.$store.state.nickname
            this.userInfo.isTeacher = this.$store.state.isTeacher
            this.userInfo.isRoomCreator = (this.roomInfo.__roomTeacherAccount === this.$store.state.account)
            this.userInfo.account = this.$store.state.account
        },
        connect: function() {
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
            this.httpServer.on('kickout', (message) => {
                this.showErrorMes(message)
                this.$router.push('/')
            })
        },
        switchPane: function(pane) {
            this.showingComponent = pane
            this.httpServer.emit('switchPane', {
                roomId: this.roomInfo.roomId,
                showingComponent: this.showingComponent
            })
        },
        startRecord: function() {
            this.captureAudio((audio) => {
                this.captureScreen((screen) => {
                    this.audioStream = audio
                    this.screenStream = screen
                    screen.width = window.screen.width
                    screen.height = window.screen.height
                    screen.fullcanvas = true
                    this.recorder = window.RecordRTC([screen, audio], {
                        type: 'video',
                        mimeType: 'video/webm',
                    })
                    this.isStoppedRecording = false
                    this.isRecordingStarted = true
                    this.recorder.startRecording()
                })
            })
        },
        stopRecord: function() {
            this.isStoppedRecording = true
            this.recorder.stopRecording(() => {
                this.leave()
                let blob = this.recorder.getBlob()
                let f = new window.File([blob], 'filename.webm')
                let formdata = new window.FormData()
                formdata.append('roomId', this.roomInfo.roomId)
                formdata.append('file', f)
                this.screenStream.stop()
                this.audioStream.stop()
                this.$store.dispatch('stopLive', formdata)
                this.$refs.recordVideo.leave()
            })
        },
        startLive: function() {
            // this.createCanvas()
            this.startRecord()
            this.$store.dispatch('startLive', {
                roomId: this.roomInfo.roomId
            })
        },
        stopLive: function() {
            this.stopRecord()
        },
        openCamera: function() {
            this.isCameraOn = true
            this.$refs.recordVideo.join()
        },
        closeCamera: function() {
            this.isCameraOn = false
            this.$refs.recordVideo.leave()
        },
        openVideo: function() {
            document.getElementById('leave').disabled = false
            document.getElementById('join').disabled = true
            this.$refs.recordVideo.join()
        },
        closeVideo: function() {
            document.getElementById('leave').disabled = true
            document.getElementById('join').disabled = false
            this.$refs.recordVideo.leave()
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
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.outer-left {
    height: 100%;
    width: 70%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.buttons {
    height: 5%;
    z-index: 100;
}

.left {
    height: 94%;
    float: left;
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
    z-index: 100;
    min-height: 36px;
}

.top-btn {
    margin: 2px;
    font-size: 10px;
    padding: 6px;
    color: #888888;
}

.right {
    width: 28%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.video-area {
    height: 70%;
    border-radius: 3px;
    border: 1px solid #e5e5e5;
    background-color: lightseagreen;
}

.chat-area {
    height: 29%;
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
