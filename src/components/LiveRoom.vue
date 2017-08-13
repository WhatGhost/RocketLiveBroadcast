<template>
    <div class="live-room" v-bind:class="{ blur: $store.state.background_blur }">
        <div class="room">
            <div class='left'>
                <el-button @click="showingComponent = 'pdfViewer'">PDF</el-button>
                <el-button @click="showingComponent = 'codeEditor'">Code Editor</el-button>
                <el-button @click="showingComponent = 'whiteBoard'">WhiteBoard</el-button>
                <pdf-viewer :hide="hidePdfViewer"></pdf-viewer>
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
            <p>{{ roomMessage }}</p>
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
                showingComponent: 'pdfViewer'
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
                return '呵呵'
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
    .live-room {
        display: flex;
        flex-direction: column;
        padding: 20px;
    }

    .room {
        top: 80px;
        flex-direction: column;
    }

    .left {
        float: left;
        border: 1px solid #3B6273;
        width: 45%;
        height: 1200px;
    }

    .right {
        width: 50%;
        float: right;
        height: 400px;
    }

    .video-area {
        height: 80%;
        border: 1px solid #3B6273;
        margin-right: -4px;
    }

    .chat-area {
        height: 50%;
        border: 1px solid #3B6273;
    }

    .message {
        display: flex;
        text-align: left;
        background-color: yellow;
    }
</style>
