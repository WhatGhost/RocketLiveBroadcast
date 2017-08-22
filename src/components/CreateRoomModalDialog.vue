<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="$store.state.showCreateRoom">
                <div class="modal-wrapper">
                    <div class="container">
                        <div class="header">
                            <p class="title">Create Room</p>
                            <el-button type="text" class="close-btn" @click="closeDialog"
                                       v-bind:class="{ disvisible: hideCloseButton }">×
                            </el-button>
                        </div>
                        <form class="form" @submit.prevent="createBtnClick" enctype="multipart/form-data">
                            <div class="function-panel">
                                <div class="upload-page" v-if="showUploadImage">
                                    <croppa v-model="myCroppa"
                                            class="cropper"
                                            canvas-color="#e8e8e8"
                                            :width="290"
                                            :height="220"
                                            :initial-image="choosedImg"
                                            :prevent-white-space="true"
                                    ></croppa>
                                    <p class="tip">
                                        鼠标滚轮：缩放图片　　
                                        左键拖动：移动图片
                                    </p>
                                </div>
                                <div class="form-page" v-if="showFillForm">
                                    <input class="name" placeholder="Room Name " v-model="roomName"/>
                                    <textarea class="introduction"
                                              placeholder="Room Introduce (optional)" v-model="roomIntroduction">
                                    </textarea>
                                </div>
                                <div class="result-page" v-if="showGetId">
                                    <h1 class="room-id">{{ openRoomResult }}</h1>
                                </div>
                            </div>
                            <input type="submit" ref="submitButton" style="display: none;">
                        </form>
                        <div class="back-next-btns">
                            <el-button type="text" class="sure-btn back-btn" v-if="canGoBack" @click="goBack">Back
                            </el-button>
                            <el-button type="text" class="sure-btn" @click="nextBtnFun">{{ nextBtnText }}</el-button>
                        </div>
                        <el-steps class="progress" :space="160" :active="step" finish-status="success">
                            <el-step description="Upload Page Image"></el-step>
                            <el-step description="Fill Information"></el-step>
                            <el-step description="Confirm ID"></el-step>
                        </el-steps>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import api from '../store/api'

const apiRoot = 'http://localhost:8000' // This will change if you deploy later

const ImagePage = 0
const FormPage = 1
const IdPage = 2

export default {
    components: {},
    data: function () {
        return {
            myCroppa: null,
            // nowView: 0. upload image; 1. fill info form; 2. comfirm room ID
            nowView: 0,
            step: 0,
            roomId: -2,
            roomName: '',
            roomIntroduction: '',
            choosedImg: null,
            // 确认创建房间失败
            openFail: false
        }
    },
    computed: {
        showUploadImage: function () {
            return this.nowView === ImagePage
        },
        showFillForm: function () {
            return this.nowView === FormPage
        },
        showGetId: function () {
            return this.nowView === IdPage
        },
        canGoBack: function () {
            return this.nowView === FormPage
        },
        hideCloseButton: function () {
            return this.nowView === 2
        },
        openRoomResult: function () {
            if (this.openFail) {
                return 'We\'re Sorry But Open Room Failed'
            }
            if (this.roomId === -2) {
                return 'Please waiting...'
            } else {
                return 'Your Room ID Is: ' + this.roomId
            }
        },
        nextBtnText: function () {
            if (this.nowView === IdPage) {
                // create room failed
                if (this.roomId === -1) {
                    return 'Close'
                } else {
                    // success
                    return 'Enter'
                }
            } else {
                return 'Next'
            }
        }
    },
    methods: {
        closeDialog: function () {
            this.$store.dispatch('closeCreateRoomDialog')
            this.nowView = 0
            this.choosedImg = null
            this.openFail = false
        },
        checkFormInput: function () {
            if (this.roomName === '') {
                this.$message({
                    message: '必须填写房间名称！',
                    type: 'error'
                })
                return false
            }
            if (this.roomIntroduction === '') {
                this.roomIntroduction = '暂无描述'
            }
            return true
        },
        nextBtnFun: function (event) {
            if (this.nowView === ImagePage || this.nowView === IdPage) {
                if (this.nowView === ImagePage) {
                    if (!this.generateImage()) {
                        return
                    }
                }
                // default image allowed
                this.goNext()
            } else if (this.nowView === FormPage) {
                // 在表单页含有检查房间名的操作，并且使用
                if (!this.checkFormInput()) {
                    return
                }
                this.$refs.submitButton.click()
                this.goNext()
            }
        },
        createBtnClick: function (event) {
            let formData = new window.FormData()
            formData.append('file-upload', this.choosedImg)
            formData.append('room-name', this.roomName)
            formData.append('room-introduction', this.roomIntroduction)
            api.post(apiRoot + '/liveroom/', formData)
                .then((response) => {
                    this.roomId = response.body.id
                    this.step = 3
                })
                .catch((error) => {
                    this.$message({
                        message: '房间创建失败' + error.detail,
                        type: 'error'
                    })
                    this.openFail = true
                })
        },
        // 页面的相关检查在上层函数完成，本函数仅用于向下翻页
        goNext: function () {
            if (this.nowView < IdPage) {
                this.nowView += 1
                this.step += 1
            } else {
                this.$store.dispatch('getRooms').then(() => {
                    this.closeDialog()
                    this.$router.push('/room/' + this.roomId)
                })
            }
        },
        goBack: function () {
            this.nowView -= 1
            this.step -= 1
        },
        generateImage: function () {
            this.choosedImg = this.myCroppa.generateDataUrl()
            if (!this.choosedImg || this.choosedImg === '') {
                this.$message({
                    message: 'Please upload your picture!',
                    type: 'error'
                })
                return false
            }
            return true
        }
    }
}
</script>

<style scoped>
.container {
    width: 480px;
    height: 460px;
    margin: 0 auto;
    background-color: #fff;
    border-radius: 20px;
    box-shadow: 0 12px 25px -6px rgba(0, 0, 0, .35);
    transition: all .3s ease;
    display: flex;
    flex-direction: column;
    /*成为包含块：用于子元素的绝对定位*/
    position: relative;
}

.header {
    margin-left: -60px;
    margin-top: 20px;
    display: flex;
    justify-content: space-around;
}

.title {
    font-size: 20px;
    text-align: left;
}

.close-btn {
    color: #cacaca;
    font-size: 30px;
    position: relative;
    left: 110px;
    margin-top: 10px;
}

.form {
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.function-panel {
    display: flex;
    flex-direction: column;
    justify-content: center;
    margin-bottom: -10px;
}

.cropper {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.croppa-container {
    margin-left: auto;
    margin-right: auto;
}

.upload-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.tip {
    margin-left: auto;
    margin-right: auto;
    font-size: 12px;
    color: #888888;
}

.form-page {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 15px;
    width: 360px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 20px;
    padding-left: 0.2em;
}

.introduction {
    width: 340px;
    height: 196px;
    resize: none;
    outline: none;
    margin-left: auto;
    margin-right: auto;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #eeeeee;
}

.result-page {
    text-align: center;
    color: #f4c20b;
    margin-top: 80px;
}

.back-next-btns {
    margin-right: auto;
    margin-left: auto;
    display: flex;
    flex-direction: row;
}

.sure-btn {
    color: lightseagreen;
    font-size: 20px;
    margin-top: 5px;
}

.back-btn {
    color: #aa8866;
}

.progress {
    position: absolute;
    left: 50px;
    bottom: 15px;
}

.disvisible {
    opacity: 0;
}
</style>
