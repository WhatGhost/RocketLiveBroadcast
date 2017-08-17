<template>
    <div class="main-div" :class="{ hiding: hide }">
        <div class="slide-upload" ref="uploadArea" v-if="!uploadedToBackend">
            <el-upload
                action="http://localhost:8000/slide/"
                drag
                name="slide"
                accept=".pptx,.ppt,.key"
                :on-success="uploadSuccess"
                :on-error="uploadError"
                :data="getRoomId">
                <i class="el-icon-upload"></i>
                <div class="el-upload-text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload-tip" slot="tip">支持PPT/PPTX/KEY格式文件</div>
            </el-upload>
        </div>
        <el-button @click="convertToPdf">get</el-button>
        <el-button @click="getPdf">real-get</el-button>
        <div class="converting-tip" v-if="converting">
            <h1>Converting, please waiting...</h1>
        </div>
        <div class="pdf-view" v-if="$store.state.finishSlide">
            <pdf :src="pdfSource" :page=page ref="pdf" @numPages="numPages=$event"></pdf>
            <div :class="userInfo.isRoomCreator?'':'hiding'">
                <button @click="pgup">Previous Page</button>
                <button @click="pgdn">Next Page</button>
                <input v-model.number="page" type="number" style="width: 5em"> /{{ numPages }}
            </div>
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
            pdfSource: '',
            uploadedToBackend: false,
            page: 1,
            numpages: 0
        }
    },
    computed: {
        converting: function () {
            if (this.uploadedToBackend && !this.$store.state.finishSlideAll) {
                return true
            }
        },
        getRoomId: function () {
            return {
                'roomId': this.roomInfo.roomId
            }
        }
    },
    created () {
        this.httpServer.on('changePage', (obj) => {
            this.page = obj.page
        })
        this.httpServer.emit('getCurrentData', {
            roomId: this.roomInfo.roomId
        })
    },
    methods: {
        pgup: function () {
            this.page = this.page - 1
            this.emitPageChange()
        },
        pgdn: function () {
            this.page = this.page + 1
            this.emitPageChange()
        },
        emitPageChange: function () {
            this.httpServer.emit('changePage', {
                roomId: this.roomInfo.roomId,
                page: this.page
            })
        },
        uploadSuccess: function () {
            this.$loading({
                target: this.$refs.uploadArea
            })
        },
        uploadError: function () {
            this.$errors()
        },
        convertToPdf: function () {
            api.patch('http://localhost:8000/slide/convert/', {
                roomId: this.roomInfo.roomId
            }).then((response) => {
                window.alert('got pdf')
            }).catch((error) => this.$message(error))
        },
        getPdf: function () {
            api.patch('http://localhost:8000/slide/get_pdf/', {
                roomId: this.roomInfo.roomId
            }).then((response) => {
                window.alert('got pdf')
                this.$store.dispatch('showPdfView')
                this.pdfSource = response.data.converted_pdf
            }).catch((error) => this.$message(error))
        }
    }
}
</script>

<style scoped>
.hiding {
    display: none;
}
</style>
