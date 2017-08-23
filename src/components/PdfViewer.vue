<template>
    <!--hide用于切换标签-->
    <div class="main-div" :class="{ hiding: hide }">
        <!--显示条件：是创建者 且 (未完成转换 或 未上传)-->
        <div class="slide-upload" ref="loadingArea" v-if="showUploadButton">
            <el-upload
                action="http://localhost:8000/slide/"
                drag
                name="slide"
                accept=".pptx,.ppt,.key"
                :on-success="uploadSuccess"
                :on-error="uploadError"
                :data="getRoomId">
                <i class="el-icon-upload"></i>
                <div class="el-upload-text">将文件拖到此处，或点击上传</div>
                <div class="el-upload-tip" slot="tip">支持PPT/PPTX/KEY格式文件</div>
            </el-upload>
        </div>
        <div class="pdf-view" v-if="pdfSource !== ''">
            <pdf :src="pdfSource" :page=page @numPages="setAllPage"></pdf>
            <div :class="userInfo.isRoomCreator?'':'hiding'">
                <button @click="pgup">Previous Page</button>
                <button @click="pgdn">Next Page</button>
                <!-- <input v-model.number="page" type="number" style="width: 5em">  -->
                <span> {{ page }} /{{ numpages }} </span>
            </div>
        </div>
        <div class="no-pdf" v-if="pdfSource === ''">
            <h1>No Slide Now</h1>
        </div>
    </div>
</template>

<script>
import pdf from 'vue-pdf'
import api from '../store/api.js'

export default {
    props: ['hide', 'httpServer', 'roomInfo', 'userInfo'],
    components: {
        pdf: pdf
    },
    data: function () {
        return {
            // loading组件的实例，通过.close()来关闭它
            loadingItem: null,
            // pdf viewer所加载的资源，由getPdf方法从后端请求得到
            pdfSource: '',
            page: 1,
            numpages: 0,
        }
    },
    computed: {
        getRoomId: function () {
            return {
                'roomId': this.roomInfo.roomId
            }
        },
        showUploadButton: function () {
            // 需要时房间创建者
            if (this.userInfo.isRoomCreator) {
                // 未获取到PDF资源：未上传或正在转换
                if (this.pdfSource === '') {
                    return true
                }
            }
            return false
        }
    },
    created () {
        // 发出获取PDF的请求， 尝试加载PDF资源
        this.getPdf()
        this.httpServer.on('changePage', (obj) => {
            this.page = obj.page
        })
    },
    methods: {
        setAllPage: function (event) {
            this.numpages = event
        },
        pgup: function () {
            if (this.page > 1) {
                this.page = this.page - 1
                this.emitPageChange()
            }
        },
        pgdn: function () {
            if (this.page < this.numpages) {
                this.page = this.page + 1
                this.emitPageChange()
            }
        },
        emitPageChange: function () {
            this.httpServer.emit('changePage', {
                roomId: this.roomInfo.roomId,
                page: this.page
            })
        },
        showErrorMes: function (mes) {
            this.$message({
                message: mes,
                type: 'warning'
            })
        },
        uploadSuccess: function () {
            this.loadingItem = this.$loading({
                target: this.$refs.loadingArea,
                text: '拼命加载中'
            })
            // 请求转换PPT
            this.convertToPdf()
        },
        uploadError: function () {
            this.showErrorMes('Something went wrong while uploading')
            this.loadingItem.close()
        },
        // 教师端发出转换命令
        convertToPdf: function () {
            api.patch('http://localhost:8000/slide/convert/', {
                roomId: this.roomInfo.roomId
            }).then((response) => {
                // 教师端获取PDF
                this.getPdf()
            }).catch((error) => this.convertError(error))
        },
        convertError: function (error) {
            this.loadingItem.close()
            this.showErrorMes(error)
        },
        // 获取PDF资源，如果没有得到仍未''
        getPdf: function () {
            api.patch('http://localhost:8000/slide/get_pdf/', {
                roomId: this.roomInfo.roomId
            }).then((response) => {
                if (response.data === 'no pdf') {
                    this.pdfSource = ''
                } else {
                    // 提供PDF资源
                    this.pdfSource = response.data.converted_pdf
                }
                // 将loading组件关掉
                if (this.loadingItem !== null) {
                    this.loadingItem.close()
                }
            }).catch((error) => this.getPdfError(error))
        },
        getPdfError: function (error) {
            this.showErrorMes('不明原因的错误：' + error)
        }
    }
}
</script>

<style scoped>
.hiding {
    display: none;
}
</style>
