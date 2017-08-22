<template>
    <div class="main-div">
        <div>
            巴拉拉能量
            <a>古娜拉黑暗之神</a>
        </div>       
        <div id="div_join" class="panel panel-default">
            <div class="panel-body">
                Channel: <input id="channel" type="text" value="1000" size="4"></input>
                Host: <input id="video" type="checkbox" checked></input>
                <button id="join" class="btn btn-primary" @click="join">Join</button>
                <button id="leave" class="btn btn-primary" @click="leave">Leave</button>
                <button id="publish" class="btn btn-primary" @click="publish">Publish</button>
                <button id="unpublish" class="btn btn-primary" @click="unpublish">Unpublish</button>
            </div>
        </div>
        <div id="video" style="margin:0 auto;">
            <div id="agora_local" style="float:left;width:300px;height:300px;display:inline-block;"></div>
        </div>
        <div>
            <div id="agora_student" style="float:left; width:300px;height:300px;display:inline-block;"></div>
        </div>
    </div>
</template>

<script>
let key = '52f1b5f55b584260b57a03744c1cdba2'
let dynamic_key = null
let localStream,client
let channelKey = "";
export default {
    props: ['userInfo', 'roomInfo'],
    data: function () {
        return {
        }
    },
    created: function () {
    },
    methods: {
        init: function () {
        },
        join: function () {
            console.log("Init AgoraRTC client with vendor key: " + key);
            client = AgoraRTC.createClient({
                mode: 'interop'
            });
            let that = this
            client.init(key, function () {
                console.log("AgoraRTC client initialized");
                client.join(dynamic_key, that.roomInfo.roomId.toString(), that.userInfo.account, function (uid) {
                    console.log("User " + uid + " join channel successfully");

                    if (document.getElementById("video").checked) {
                        console.log('获取本地流')
                        localStream = AgoraRTC.createStream({
                            streamID: uid,
                            audio: true,
                            video: true,
                            screen: false
                        });
                        if (document.getElementById("video").checked) {
                            console.log('设置清晰度')
                            localStream.setVideoProfile('720p_3');
                        }
                        localStream.init(function () {
                            console.log("getUserMedia successfully");
                            localStream.play('agora_local');

                            client.publish(localStream, function (err) {
                                console.log("Publish local stream error: " + err);
                            });

                            client.on('stream-published', function (evt) {
                                console.log("Publish local stream successfully");
                            });
                        }, function (err) {
                            console.log("getUserMedia failed", err);
                        });
                    }
                }, function (err) {
                    console.log("Join channel failed", err);
                });
            }, function (err) {
                console.log("AgoraRTC client init failed", err);
            });


            client.on('error', function (err) {
                console.log("Got error msg:", err.reason);
                if (err.reason === 'DYNAMIC_KEY_TIMEOUT') {
                    client.renewChannelKey(channelKey, function () {
                        console.log("Renew channel key successfully");
                    }, function (err) {
                        console.log("Renew channel key failed: ", err);
                    });
                }
            });
            client.on('stream-added', function (evt) {
                var stream = evt.stream;
                console.log("New stream added: " + stream.getId());
                console.log("Subscribe ", stream);
                client.subscribe(stream, function (err) {
                    console.log("Subscribe stream failed", err);
                });
            });

            client.on('stream-subscribed', function (evt) {
                var stream = evt.stream;
                console.log("Subscribe remote stream successfully: " + stream.getId());
                stream.play('agora_student');
            });

            client.on('stream-removed', function (evt) {
                var stream = evt.stream;
                stream.stop();
                console.log("Remote stream is removed " + stream.getId());
            });

            client.on('peer-leave', function (evt) {
                var stream = evt.stream;
                if (stream) {
                    stream.stop();
                    console.log(evt.uid + " leaved from this channel");
                }
            });
        },

        leave: function () {
            document.getElementById("leave").disabled = true;
            client.leave(function () {
                console.log("Leavel channel successfully");
            }, function (err) {
                console.log("Leave channel failed");
            });
        },

        publish: function () {
            document.getElementById("publish").disabled = true;
            document.getElementById("unpublish").disabled = false;
            client.publish(localStream, function (err) {
                console.log("Publish local stream error: " + err);
            });
        },

        unpublish: function () {
            document.getElementById("publish").disabled = false;
            document.getElementById("unpublish").disabled = true;
            client.unpublish(localStream, function (err) {
                console.log("Unpublish local stream failed" + err);
            });
        },

        // getDevices: function () {
        //     AgoraRTC.getDevices(function (devices) {
        //         for (var i = 0; i !== devices.length; ++i) {
        //             var device = devices[i];
        //             var option = document.createElement('option');
        //             option.value = device.deviceId;
        //             if (device.kind === 'audioinput') {
        //                 option.text = device.label || 'microphone ' + (audioSelect.length + 1);
        //                 audioSelect.appendChild(option);
        //             } else if (device.kind === 'videoinput') {
        //                 option.text = device.label || 'camera ' + (videoSelect.length + 1);
        //                 videoSelect.appendChild(option);
        //             } else {
        //                 console.log('Some other kind of source/device: ', device);
        //             }
        //         }
        //     });
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
