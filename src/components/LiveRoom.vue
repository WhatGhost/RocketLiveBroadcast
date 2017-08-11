<template>
    <div class="live-room" v-bind:class="{ blur: $store.state.background_blur }">
        <div class="button-message">
            <div>
                <el-button class="teacher-message" @click="switchMessageMenu">message</el-button>
                <el-button class="back" @click="goHomepage">Go Homepage</el-button>
            </div>
        </div>
        <div class="room">
            <p>LiveRoomPage</p>
            <div class='left'>
                <el-button @click="showingComponent = 'slide'">Slide</el-button>
                <el-button @click="showingComponent = 'codeEditor'">Code Editor</el-button>
                <el-button @click="showingComponent = 'whiteBoard'">WhiteBoard</el-button>
                <slide-page :hide="hideSlide"></slide-page>
                <code-editor-page :hide="hideCodeEditor"></code-editor-page>
                <white-board-page :hide="hideWhiteBoard"></white-board-page>
            </div>
            <div class='right'>
                <record-video class="video-area"></record-video>
                <hr>
                <chat-area class="chat-area"></chat-area>
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
                showMessageMenu: false,
                showingComponent: 'slide'
            }
        },
        computed: {
            hideSlide: function () {
                return this.showingComponent !== 'slide'
            },
            hideCodeEditor: function () {
                return this.showingComponent !== 'codeEditor'
            },
            hideWhiteBoard: function () {
                return this.showingComponent !== 'whiteBoard'
            }
        },
        methods: {
            switchMessageMenu: function () {
                this.showMessageMenu = !this.showMessageMenu
            },
            goHomepage: function () {
                // add vue rooter
            },
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
        margin-right: 20px;
    }

    .video-area {
        height: 50%;
        border: 1px solid #3B6273;
        margin-right: -4px;
    }

    .chat-area {
        height: 50%;
        border: 1px solid #3B6273;
    }
</style>
