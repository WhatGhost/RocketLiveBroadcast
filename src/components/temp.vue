<template>
    <div class="main-div" :class="{ hiding: hide }">
        <div class="slide-div">
            <div class="upload-btn-div">
                <!--<el-upload-->
                <!--action="https://jsonplaceholder.typicode.com/posts/"-->
                <!--class="upload-file"-->
                <!--drag-->
                <!--:before-upload="workBeforeUpload"-->
                <!--:data=form>-->
                <!--<i class="el-icon-upload"></i>-->
                <!--<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>-->
                <!--<div class="el-upload__tip" slot="tip">支持PPT/PPTX/WORD/EXCEL/KEY格式文件</div>-->
                <!--</el-upload>-->
                <el-upload
                    action="//up.qbox.me/"
                    drag
                    :before-upload="workBeforeUpload"
                    :on-success="handleSuccess"
                    :on-error="handleError"
                    ref="upload"
                    :data="form">
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                    <div class="el-upload__tip" slot="tip">支持PPT/PPTX/WORD/EXCEL/KEY格式文件</div>
                </el-upload>
            </div>
            <iframe class="slide-frame" v-if="finishUpload" :src="slideUrl">
            </iframe>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        'hide': false,
    },
    components: {
        // ElButton
    },
    data: function () {
        return {
            slideUrl: 'http://www.tuicool.com/',
            form: {
                token: this.$store.state.token,
                key: this.$store.state.slideKey
            }
        }
    },
    computed: {
        finishUpload: function () {
            return this.$store.state.finishSlideUpload
        },
        // convert key file
        finishConvert: function () {
        }
    },
    methods: {
        handleError: function () {
            window.alert('失败！！！')
        },
        handleSuccess: function () {
            window.alert('成了')
        },
        workBeforeUpload: function (file) {
            if (!this.checkFileRight(file)) {
                return false
            }
            // 获取上传凭证
            this.$store.dispatch('askToken', file.name)
            if (this.$store.state.token === '') {
                return
            }
            // 填写上传form
            this.form = {
                token: this.$store.state.token,
                key: this.$store.state.slideKey
            }
        },
        checkFileRight: function (file) {
            let type = file.type
            if (file.name.indexOf('.key') === file.name.length - 4) {
                this.$message.error('key播放功能开发中……敬请期待')
                return false
            }
            // eslint中的switch语句检查，要求case与switch统一缩进，但是webstorm中
            // 的默认缩进设置会改变这种缩进，导致eslint报错，取消该设置：
            // setting-codestyle-wrap-switch
            switch (type) {
            case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
            case 'application/vnd.ms-powerpoint':
            case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                return true
            default:
                this.$message.error('此格式文件暂不支持')
                return false
            }
        }
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    justify-content: center;
    flex-direction: column;
    background-color: #bce8f1;
}

.hiding {
    display: none;
}

.slide-div {
    display: flex;
    justify-content: center;
    background-color: #edecd6;
}

.slide-frame {
    margin: 20px;
    width: 600px;
    height: 400px;
}
</style>
