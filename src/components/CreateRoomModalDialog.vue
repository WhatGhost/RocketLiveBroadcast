<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="$store.state.showCreateRoom">
                <div class="modal-wrapper">
                    <div class="container">
                        <p class="title">Create Room</p>
                        <el-button type="text" class="close-btn" @click="closeDialog" v-if="this.nowView !== 2">×
                        </el-button>
                        <form @submit.prevent="createBtnClick" enctype="multipart/form-data">
                            <div class="function-panel">
                                <div class="upload-page" v-if="showUploadImage">
                                    <img id="preview" src="../assets/play.gif"/>
                                    <label for="file-upload-input" class="custom-file-upload">
                                        上传封面
                                    </label>
                                    <input id="file-upload-input" type="file" @change="imgPreview($event)"
                                           style="display: none;"/>
                                </div>
                                <div class="form-page" v-if="showFillForm">
                                    <input type="text" class="name" placeholder="Room Name "
                                           v-model="roomName"/>
                                    <textarea class="introduction"
                                              placeholder="Room Introduce (within 60 word) " v-model="roomIntroduction">
                                    </textarea>
                                </div>
                                <div class="result-page" v-if="showGetId">
                                    <h1 class="room-id">{{ openRoomResult }}</h1>
                                </div>
                            </div>
                            <input type="submit" ref="submitButton" style="display: none;">
                        </form>
                        <div class="back-next-btns">
                            <el-button class="sure-btn shadow-m" v-if="canGoBack" @click="goBack">back</el-button>
                            <el-button class="sure-btn shadow-m" @click="nextBtnFun">{{ nextBtnText }}</el-button>
                        </div>
                        <el-steps :space="100" :active="active" finish-status="success">
                            <el-step title="Upload Page Image"></el-step>
                            <el-step title="Fill Information"></el-step>
                            <el-step title="Confirm Room ID"></el-step>
                        </el-steps>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
const ImagePage = 0
const FormPage = 1
const IdPage = 2

export default {
    components: {},
    data: function () {
        return {
            // nowView: 0. upload image; 1. fill info form; 2. comfirm room ID
            nowView: 0,
            roomId: -1,
            roomName: '',
            roomIntroduction: '',
            choosedImg: null
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
        openRoomResult: function () {
            if (this.roomId === -1) {
                return 'We\'re Sorry But Open Room Failed'
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
        imgPreview (event) {
            let input = event.target
            let reader = new window.FileReader()
            reader.readAsDataURL(input.files[0])
            reader.onload = function () {
                let dataURL = reader.result
                let output = document.getElementById('preview')
                output.src = dataURL
            }
            // due to the life cycle of Vue, input which id is below
            // will really disappear when it is hiden
            this.choosedImg = document.getElementById('file-upload-input').files[0]
        },
        closeDialog: function () {
            this.$store.dispatch('closeCreateRoomDialog')
            this.nowView = 0
        },
        nextBtnFun: function (event) {
            // functions: go to next page; go to next page and submit;
            // close; close and open new page
            if (this.nowView === ImagePage || this.nowView === IdPage) {
                // default image allowed
                this.goNext()
            } else if (this.nowView === FormPage) {
                this.$refs.submitButton.click()
                this.goNext()
            }
        },
        createBtnClick: function (event) {
            let formData = new window.FormData()
            console.log('chosen image: ' + this.choosedImg)
            formData.append('file-upload', this.choosedImg)
            formData.append('room-name', this.roomName)
            formData.append('room-introduction', this.roomIntroduction)
            this.$store.dispatch('createRoom', formData).then((response) => {
                this.roomId = this.$store.state.live_room_id
            })
        },
        goNext: function () {
            if (this.nowView < IdPage) {
                this.nowView += 1
            } else {
                this.closeDialog()
                this.$router.push('/room/' + this.roomId)
            }
        },
        goBack: function () {
            this.nowView -= 1
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
}

.close-btn {
    color: #cacaca;
    font-size: 30px;
    position: relative;
    left: 70px;
    top: -14px;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 13px;
    margin-bottom: 20px;
    padding-bottom: 8px;
    padding-left: 0.2em;
}

#preview {
    width: 200px;
    height: 200px;
}

.sure-btn {
    font-size: 20px;
    background-color: #FF8C85;
    border-radius: 20px;
    margin-top: 25px;
}

.back-next-btns {
    display: flex;
    flex-direction: row;
}

.custom-file-upload {
    border: 1px solid silver;
}

textarea {
    outline: none;
    border: 1px solid silver;
}
</style>
