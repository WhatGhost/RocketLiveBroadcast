<template>
    <div class="create-room">
        <div class="left-page">
            <img id="preview" />
            <br />
            <label for="file-upload" class="custom-file-upload" onchange="imgPreview(this)">
                上传视频截图
            </label>
            <input id="file-upload" type="file" />
        </div>
        <div class="right-page">
            <div>
                <input type="text" id="room-name" placeholder="房间名称 " size="30 " />
            </div>
            <div>
                <input type="text" id="room-description" placeholder="房间介绍 " size="30 " />
            </div>
            <div class="room-id">系统为您分配的房间id为：2123221</div>
            <button id="create" onclick=alert("创建成功")>开通房间</button>
        </div>
    </div>
</template>
<script>
export default {
    methods: {
        imgPreview(fileDom) {
            let reader = new window.FileReader()
            if (window.FileReader) {
            } else {
                window.alert('您的设备不支持图片预览功能，如需该功能请升级您的设备！')
            }
            let file = fileDom.files[0]
            let imageType = /^image\//
            if (!imageType.test(file.type)) {
                window.alert('请选择图片！')
                return
            }
            reader.onload = function (e) {
                let img = document.getElementById('preview')
                img.src = e.target.result
            }
            reader.readAsDataURL(file)
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
</style>