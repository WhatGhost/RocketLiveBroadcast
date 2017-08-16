<template>
    <div class="main-div" :class="{ hiding: hide }">
        <pdf src="/static/static/review.pdf" :page=page ref="pdf" @numPages="numPages=$event"></pdf>
        <div :class="userInfo.isRoomCreator?'':'hiding'">
            <button @click="pgup">Previous Page</button>
            <button @click="pgdn">Next Page</button>
            <input v-model.number="page" type="number" style="width: 5em"> /{{ numPages }}
        </div>
    </div>
</template>

<script>
    import pdf from 'vue-pdf'
    export default {
        props: ['hide', 'httpServer', 'roomInfo', 'userInfo'],
        components: {
            pdf: pdf
        },
        data: function () {
            return {
                page: 1,
                numpages: 0
            }
        },
        created() {
            this.httpServer.on('changePage', (obj) => {
                this.page = obj.page
            })
            this.httpServer.emit('getCurrentData', {
                roomId: this.roomInfo.roomId
            })
        },
        methods: {
            pgup() {
                this.page = this.page - 1
                this.emitPageChange()
            },
            pgdn() {
                this.page = this.page + 1
                this.emitPageChange()
            },
            emitPageChange() {
                this.httpServer.emit('changePage', {
                    roomId: this.roomInfo.roomId,
                    page: this.page
                })
            }
        }
    }
</script>

<style scoped>
    .hiding {
        display: none;
    }
</style>
