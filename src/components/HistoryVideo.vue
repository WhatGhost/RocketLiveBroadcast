<template>
    <div class="main-div">
        <div class="head-tip">
            <h1>房间名称：{{ roomInfo.roomName }}</h1>
            <div class="id-teacher">
                <label>房间ID：{{ roomInfo.roomId }}</label>
                <label>　　教师：{{ roomInfo.roomTeacher }}</label>
            </div>
        </div>
        <video class="video" v-bind:src="videoSource" controls="controls">
        </video>
        <p class="bottom-intro">简介：{{ roomInfo.roomIntroduction }}</p>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            videoSource: '',
            roomInfo: {
                roomId: -1,
                roomName: '',
                roomTeacher: '',
                roomIntroduction: '',
                // 没有必要请不要访问这个变量
                __roomTeacherAccount: ''
            },
        }
    },
    methods: {
        getVideoSource: function () {
            for (let i = 0; i < this.$store.state.history.length; i++) {
                if (this.$store.state.history[i].room_id === parseInt(this.$route.params['id'])) {
                    let source = this.$store.state.history[i].history_source
                    this.videoSource = source
                    return
                }
            }
        },
        getRoomInfo: function () {
            for (let i = 0; i < this.$store.state.rooms.length; i++) {
                if (this.$store.state.history[i].room_id === parseInt(this.$route.params['id'])) {
                    this.roomInfo.roomIntroduction = this.$store.state.history[i].room_introduction
                    this.roomInfo.roomTeacher = this.$store.state.history[i].room_creator.nickname
                    this.roomInfo.roomName = this.$store.state.history[i].room_name
                    this.roomInfo.__roomTeacherAccount = this.$store.state.history[i].room_creator.account
                }
            }
            this.roomInfo.roomId = this.$route.params['id']
        },
    },
    beforeMount: function () {
        this.getVideoSource()
        this.getRoomInfo()
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
}

.video {
    width: 75%;
    margin: auto;
    border: 3px solid #d9d9d9;
}

.head-tip, .bottom-intro {
    width: 85%;
    margin: 20px auto;
    color: #888888;
}

h1 {
    color: #4f4f4f;
    margin-top: -15px;
}

.bottom-intro {
    font-size: 17px;
    color: #888888;
}
</style>
