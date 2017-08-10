<template>
    <div class="main-div" :class="{ hiding: hide }">
        <div class="slide-div">
            <div class="upload-btn-div">
                <el-upload
                    class="upload-file"
                    action="http://localhost:8000/liveroom/"
                    :file-list="fileList">
                    <el-button size="small" type="primary">点击上传演示文档</el-button>
                    <div slot="tip" class="el-upload__tip">支持PPT、PPTX、Key文件，且不超过500MB</div>
                </el-upload>
            </div>
            <iframe class="slide-frame" v-if="finishUpload" :src="slideUrl">
            </iframe>
        </div>
    </div>
</template>

<script>
    import ElButton from '../../node_modules/element-ui/packages/button/src/button.vue'

    export default {
        props: {
            'hide': false,
        },
        components: {
            ElButton
        },
        data: function () {
            return {
                slideUrl: 'http://www.tuicool.com/a/'
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
