<template>
    <div class="live-room">
        <div class="button-message">
            <div>
                <el-button class="teacher-message" @click="switchMessageMenu">message</el-button>
                <el-button class="back" @click="goHomepage">Go Homepage</el-button>
            </div>
        </div>
        <div class="room">
            <p>LiveRoomPage</p>
            <div class='left'>
                <el-button @click="currentView = 'SlidePage'">Slide</el-button>
                <el-button @click="currentView = 'CodeEditorPage'">Code Editor</el-button>
                <el-button @click="currentView = 'WhiteBoardPage'">WhiteBoard</el-button>
                <component :is='currentView'></component>
            </div>
            <div class='right'>
                <record-video></record-video>
                <hr>
                <chat-area></chat-area>
            </div>
        </div>
        <div class="message">
            <live-room-menu v-if="showMessageMenu"></live-room-menu>
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

    export default {
        components: {
            LiveRoomMenu,
            SlidePage,
            WhiteBoardPage,
            CodeEditorPage,
            RecordVideo,
            ChatArea
        },
        data: function () {
            return {
                currentView: 'SlidePage',
                showMessageMenu: false
            }
        },
        methods: {
            switchMessageMenu: function () {
                this.showMessageMenu = !this.showMessageMenu
            },
            goHomepage: function () {
                // add vue rooter
            }
        }
    }
</script>

<style scoped>
    .teacher-message {
        float: left;
        height: 30px;
    }

    .back {
        top: 10px;
        float: left;
        height: 30px;
    }

    .message {
        display: flex;
        position: absolute;
        left: 20px;
        top: 120px;
        background-color: silver;
        text-align: left;
    }

    .room {
        top: 80px;
        padding-left: 20px;
        flex-direction: column;
    }

    .left {
        float: left;
        border: 1px solid #3B6273;
        margin-right: -4px;
        width: 600px;
        height: 500px;
    }

    .right {
        width: 50%;
        float: right;
        height: 400px;
        border: 1px solid #3B6273;
        margin-right: -4px;
    }

    .video {
        height: 50%;
        border: 1px solid #3B6273;
        margin-right: -4px;
    }

    .chat-area {
        height: 50%;
        border: 1px solid #3B6273;
    }
</style>


