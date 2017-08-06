<template>
    <div class="create-room">
        <form @submit.prevent="createBtnClick" enctype="multipart/form-data" method="POST">
            <div class="left-page">
                <label for="file-upload" class="custom-file-upload">
                    上传视频截图
                </label>
                <input id="file-upload" name="file-upload" type="file" @change="imgPreview($event)" />
                <img id="preview" />
                <br/>
            </div>
            <div class="right-page">
                <div>
                    <input type="text" id="room-name" name="room-name" placeholder="房间名称 " size="30 " v-model="room_name" />
                </div>
                <div>
                    <input type="text" id="room-description" name="room-description" placeholder="房间介绍 " size="30" v-model="room_introduction" />
                </div>
                <div class="room-id">系统为您分配的房间id为：</div>
                <input type="submit" id="create" value="开通房间">
            </div>
        </form>
    </div>
</template>
<script>
export default {
    data: function () {
        return {
            room_name: '',
            room_introduction: '',
            room_creater: '',
        }
    },
    methods: {
        imgPreview(event) {
            let input = event.target
            let reader = new window.FileReader()
            reader.readAsDataURL(input.files[0])
            reader.onload = function () {
                let dataURL = reader.result
                let output = document.getElementById('preview')
                output.src = dataURL
            }
        },
        createBtnClick: function (event) {
            // let roomId = -1
            // console.log(document.getElementById('file-upload').value)
            // this.$store.dispatch('createRoom', {
            //     room_name: this.room_name,
            //     room_introduction: this.room_introduction,
            //     room_img: document.getElementById('file-upload').value,
            //     room_creater: 'wanglitong'
            // }).then(() => {
            //     roomId = this.$store.state.live_room_id
            //     window.alert('创建成功' + roomId)
            // })
            let formData = new window.FormData(event.target)
            console.log('start..')
            // for (let element of formData) {
            //     console.log(element)
            // }
            console.log(formData.entries)
            console.log('end..')
            this.$store.dispatch('createRoom', formData).then(() => {
                let roomId = this.$store.state.live_room_id
                window.alert('创建成功' + roomId)
            })
        }
    }
}
</script>
<style scoped>
.create-room {
    height: 300px;
    width: 700px;
    border: 5px solid black;
}

.left-page {
    width: 40%;
    float: left;
}

.right-page {
    width: 60%;
    float: left;
}

#room-name {
    margin-top: 20px;
    height: 30px;
}

#room-description {
    margin-top: 20px;
    height: 80px;
}

.room-id {
    margin-top: 20px;
}

#create {
    margin-left: 120px;
    height: 40px;
    width: 120px;
    margin-top: 40px;
    color: white;
    background-color: green;
    background: -moz-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* FF3.6+ */
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #a5cd4e), color-stop(100%, #6b8f1a));
    /* Chrome,Safari4+ */
    background: -webkit-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* Chrome10+,Safari5.1+ */
    background: -o-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* Opera 11.10+ */
    background: -ms-linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* IE10+ */
    background: linear-gradient(top, #a5cd4e 0%, #6b8f1a 100%);
    /* W3C */
}

input[type="file"] {
    display: none;
}

.custom-file-upload {
    margin-top: 150px;
    border: 1px solid #ccc;
    display: inline-block;
    padding: 6px 12px;
    cursor: pointer;
}

#preview {
    height: 150px;
    width: 150px;
}
</style>