<template>
    <div class="main-div">
        <h1>Recording</h1>
        <div>
            <button onclick="teacherInit()">btn</button>
            <div id="otherClients"> </div>
            <video style="float:left" :class="displayTea" id="self" width="300" height="200"></video>
            <video style="float:left" :class="displayStu" id="caller" width="300" height="200"></video>
        </div>
    </div>
</template>

<script>
// import {disconnect, studentInit, teacherInit} from '../../static/rtclogic.js'
// import teacherInit from '../../static/rtclogic.js'
// import studentInit from '../../static/rtclogic.js'

export default {
    props: ['userInfo', 'roomInfo'],
    data: function () {
        return {
            displayTea: 'display',
            displayStu: 'display',
        }
    },
    created: function () {
        if (this.userInfo.isRoomCreator) {
            this.displayTea = 'display'
            this.displayStu = 'hidden'
        } else {
            this.displayTea = 'hidden'
            this.displayStu = 'display'
        }
    },
    methods: {
        // init: function () {
        //     if (this.userInfo.isRoomCreator) {
        //         teacherInit()
        //     } else {
        //         studentInit()
        //     }
        // }
    }
}
</script>

<style scoped>
.main-div {}

.hidden {
    display: none;
}
</style>
