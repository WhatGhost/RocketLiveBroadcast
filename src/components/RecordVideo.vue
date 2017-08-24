<template>
    <div class="main-div">
        <div id="div_join" class="panel panel-default">
            <div class="panel-body">
                <!-- <button id="join" :class="studentDisplay" @click="join">打开视频</button>
                <button id="leave" :class="studentDisplay" @click="leave">关闭视频</button> -->
                <!-- <button id="publish" :class="teacherDisplay" @click="publish">继续直播</button>
                <button id="unpublish" :class="teacherDisplay" @click="unpublish">暂停直播</button> -->
            </div>
        </div>
        <div id="video" style="margin:0 auto;">
            <div id="agora_teacher" class="hidden" style="float:left;width:300px;height:300px;"></div>
            <!-- <video controls "width:33%;position:absolute;right:40%; background-color:black;" src="video.webm" loop autoplay></video> -->
            <video id="camera" :class="teacherDisplay" style="width:100%;height:100%;background-color:black;"></video>
        </div>
        <div>
            <div id="agora_student" :class="studentDisplay" style="float:left; width:300px;height:300px;"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['userInfo', 'roomInfo'],
    data: function () {
        return {
            key: '52f1b5f55b584260b57a03744c1cdba2',
            dynamic_key: null,
            localStream: '',
            client: '',
            channelKey: '',
            teacherDisplay: '',
            studentDisplay: '',
            videoElement: '',
        }
    },
    mounted: function () {
        if (this.userInfo.isRoomCreator) {
            this.studentDisplay = 'hidden'
        } else {
            this.teacherDisplay = 'hidden'
            this.studentJoin()
        }
    },
    methods: {
        initLocal: function () {
            this.videoElement = document.querySelector('#camera')
            console.log("Init local camera")
            let that = this
            function successCallback(stream) {
                that.videoElement.stream = stream;
                that.videoElement.onloadedmetadata = function() {

                };
                that.videoElement.src = URL.createObjectURL(stream);
                that.videoElement.play();
            }
            function errorCallback(error) {
                console.error('get-user-media error', error);

            }
            var mediaConstraints = { video: true };
            navigator.mediaDevices.getUserMedia(mediaConstraints).then(successCallback).catch(errorCallback);
        },
        stopLocalCamera: function () {
            this.videoElement = document.querySelector('#camera')
            this.videoElement.stream.getTracks().forEach(function(track) {
                track.stop();
            });
        },
        join: function () {
            if (this.userInfo.isRoomCreator) {
                console.log(123123)
                this.teacherJoin()
                // this.initLocal()
            } else {
                this.studentJoin()
            }
        },
        teacherJoin: function () {
            console.log("Init AgoraRTC client with vendor key: " + this.key);
            document.getElementById("leave").disabled = false
            document.getElementById("join").disabled = true
            this.client = AgoraRTC.createClient({
                mode: 'interop'
            });
            let that = this
            this.client.init(this.key, function () {
                console.log("AgoraRTC client initialized")
                that.client.join(that.dynamic_key, that.roomInfo.roomId.toString(), that.userInfo.account, function (uid) {
                    console.log("User " + uid + " join channel successfully")
                    console.log('获取本地流')
                    that.localStream = AgoraRTC.createStream({
                        streamID: uid,
                        audio: true,
                        video: true,
                        screen: false
                    });
                    console.log('设置清晰度')
                    that.localStream.setVideoProfile('480p_6')
                    that.localStream.init(function () {
                        console.log("getUserMedia successfully")
                        that.localStream.play('agora_teacher')
                        that.client.publish(that.localStream, function (err) {
                            console.log("Publish local stream error: " + err)
                        });
                        that.client.on('stream-published', function (evt) {
                            console.log("Publish local stream successfully")
                        });
                        that.initLocal()
                    }, function (err) {
                        console.log("getUserMedia failed", err)
                    });
                }, function (err) {
                    console.log("Join channel failed", err)
                });
            }, function (err) {
                console.log("AgoraRTC client init failed", err)
            });
            this.client.on('error', function (err) { that.occurError(err) })
            this.client.on('stream-added', function (evt) { that.streamAdd(evt) })
            this.client.on('stream-subscribed', function (evt) { that.streamSubscribed(evt) })
            this.client.on('stream-removed', function (evt) { that.streamRemoved(evt) })
            this.client.on('peer-leave', function (evt) { that.peerLeave(evt) })
        },
        studentJoin: function () {
            console.log("Init AgoraRTC client with vendor key: " + this.key);
            document.getElementById("leave").disabled = false
            document.getElementById("join").disabled = true
            this.client = AgoraRTC.createClient({
                mode: 'interop'
            });
            let that = this
            this.client.init(this.key, function () {
                console.log("AgoraRTC client initialized");
                that.client.join(that.dynamic_key, that.roomInfo.roomId.toString(), that.userInfo.account, function (uid) {
                    console.log("User " + uid + " join channel successfully");
                }, function (err) {
                    console.log("Join channel failed", err)
                })
            }, function (err) {
                console.log("AgoraRTC client init failed", err)
            })
            this.client.on('error', function (err) { that.occurError(err) })
            this.client.on('stream-added', function (evt) { that.streamAdd(evt) })
            this.client.on('stream-subscribed', function (evt) { that.streamSubscribed(evt) })
            this.client.on('stream-removed', function (evt) { that.streamRemoved(evt) })
            this.client.on('peer-leave', function (evt) { that.peerLeave(evt) })
        },
        streamAdd: function (evt) {
            var stream = evt.stream;
            console.log("New stream added: " + stream.getId());
            console.log("Subscribe ", stream);
            this.client.subscribe(stream, function (err) {
                console.log("Subscribe stream failed", err);
            });
        },
        streamSubscribed: function (evt) {
            var stream = evt.stream;
            console.log("Subscribe remote stream successfully: " + stream.getId());
            stream.play('agora_student');
        },
        streamRemoved: function (evt) {
            var stream = evt.stream;
            stream.stop();
            console.log("Remote stream is removed " + stream.getId());
        },
        peerLeave: function (evt) {
            var stream = evt.stream;
            if (stream) {
                stream.stop();
                console.log(evt.uid + " leaved from this channel");
            }
        },
        occurError: function (err) {
            console.log("Got error msg:", err.reason)
            if (err.reason === 'DYNAMIC_KEY_TIMEOUT') {
                this.client.renewChannelKey(that.channelKey, function () {
                    console.log("Renew channel key successfully")
                }, function (err) {
                    console.log("Renew channel key failed: ", err)
                })
            }
        },
        leave: function () {
            if (this.userInfo.isRoomCreator) {
                this.localStream.disableVideo()
                this.localStream.close()
            } else {
                document.getElementById('leave').disabled = true
                document.getElementById('join').disabled = false
            }
            this.client.leave(function () {
                console.log("Leavel channel successfully")
            }, function (err) {
                console.log("Leave channel failed")
            });
        },

        publish: function () {
            if (this.userInfo.isRoomCreator) {
                this.localStream.enableVideo()
            }
            // document.getElementById("publish").disabled = true;
            // document.getElementById("unpublish").disabled = false;
            this.client.publish(this.localStream, function (err) {
                console.log("Publish local stream error: " + err);
            });
            this.initLocal()
        },

        unpublish: function () {
            if (this.userInfo.isRoomCreator) {
                this.localStream.disableVideo()
            }
            // document.getElementById("publish").disabled = false;
            // document.getElementById("unpublish").disabled = true;
            this.client.unpublish(this.localStream, function (err) {
                console.log("Unpublish local stream failed" + err);
            });
            this.stopLocalCamera()
        },
    }
}
</script>

<style scoped>
.main-div {}

.hidden {
    display: none;
}
</style>
