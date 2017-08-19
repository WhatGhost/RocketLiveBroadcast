<template>
    <div class="main-div">
        <h1>Recording</h1>
        <div>
            <button @click="init">btn</button>
            <div id="otherClients"> </div>
            <video style="float:left" :class="displayTea" id="self" width="300" height="200"></video>
            <video style="float:left" :class="displayStu" id="caller" width="300" height="200"></video>
        </div>
    </div>
</template>

<script>
easyrtc.setStreamAcceptor(function (callerEasyrtcid, stream) {
    var video = document.getElementById('caller');
    easyrtc.setVideoObjectSrc(video, stream);
});

easyrtc.setOnStreamClosed(function (callerEasyrtcid) {
    easyrtc.setVideoObjectSrc(document.getElementById('caller'), "");
});


function teacherInit(roomId) {
    easyrtc.setRoomOccupantListener(loggedInListener);
    var connectSuccess = function (myId) {
    }
    var connectFailure = function (errorCode, errText) {
    }
    easyrtc.initMediaSource(
        function () { // success callback
            var selfVideo = document.getElementById("self");
            easyrtc.setVideoObjectSrc(selfVideo, easyrtc.getLocalStream());
            easyrtc.connect(roomId, connectSuccess, connectFailure);
        },
        connectFailure
    );

}
function studentInit(roomId) {
    easyrtc.setRoomOccupantListener(loggedInListener);
    var connectSuccess = function (myId) {
    }
    var connectFailure = function (errorCode, errText) {
    }
    easyrtc.enableAudio(false);
    // easyrtc.enableVideo(false);
    easyrtc.initMediaSource(
        function () { // success callback
            var selfVideo = document.getElementById("self");
            easyrtc.setVideoObjectSrc(selfVideo, easyrtc.getLocalStream());
            easyrtc.connect(roomId, connectSuccess, connectFailure);
        },
        connectFailure
    );
    MediaStream.getTracks()[1].stop();
}


function loggedInListener(roomName, otherPeers) {
    var otherClientDiv = document.getElementById('otherClients');
    while (otherClientDiv.hasChildNodes()) {
        otherClientDiv.removeChild(otherClientDiv.lastChild);
    }
    for (var i in otherPeers) {
        var button = document.createElement('button');
        button.onclick = function (easyrtcid) {
            return function () {
                performCall(easyrtcid);
            }
        }(i);

        let label = document.createTextNode(i);
        button.appendChild(label);
        otherClientDiv.appendChild(button);
    }
}


function performCall(easyrtcid) {
    easyrtc.call(
        easyrtcid,
        function (easyrtcid) {
        },
        function (errorCode, errorText) {
        },
        function (accepted, bywho) {
        }
    );
}
function disconnect() {
    easyrtc.clearMediaStream( document.getElementById('self'));
    easyrtc.clearMediaStream( document.getElementById('caller'));
    easyrtc.disconnect()
    MediaStream.getTracks()[1].stop();

}
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
        init: function () {
            if (this.userInfo.isRoomCreator) {
                teacherInit(this.roomInfo.roomId.toString())
            } else {
                studentInit(this.roomInfo.roomId.toString())
            }
        }
    }
}
</script>

<style scoped>
.main-div {}

.hidden {
    display: none;
}
</style>
