<template>
    <div class="live-room">
        <div class="button-message">
            <div>
                <button class="teacher-message" @click="changePage">message</button>
                <button class="back" @click="currentView=''">back</button>
            </div>
            </br>
            <div class="message">
                <component @click="changePage" :is='currentView'></component>
            </div>
        </div>
        <div class="room">    
            <p>LiveRoomPage</p>
            <div class='left'>
                <button></button>
                <button></button>
                <button></button>
            </div>
            <div class='right'>
                <div class='vedio'>
                </div>
                <div class='code-editor'></div>
            </div>
        </div>
    </div>
</template>

<script>
import LiveRoomMenu from './LiveRoomMenu'
export default {
    components: {
        LiveRoomMenu,
    },
    data: function () {
        return {
            currentView: ''
        }
    },
    methods: {
        changePage: function () {
            this.currentView = LiveRoomMenu
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
        top: 100px;
        display: flex;
        justify-content: left;
        width: 30%;
    }

    .room {
        position: absolute;
        top: 80px;
        padding-left: 300px;
        width: 400px;
        flex-direction: column;
        width: 70%;
    }

    .left {
        width: 50%;
        float: left;
        height: 400px;
        border: 1px solid #3B6273;
        margin-right: -4px;
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

    .code-editor {
        height: 50%;
        border: 1px solid #3B6273;
    }
</style>


