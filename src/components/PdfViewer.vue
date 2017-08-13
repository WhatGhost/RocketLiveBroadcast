<template>
    <div class="main-div" :class="{ hiding: hide }">
        <button @click="pgup">Previous Page</button>
        <button @click="pgdn">Next Page</button>
        <input v-model.number="page" type="number" style="width: 5em"> /{{ numPages }}
        <pdf src="../static/review.pdf" :page=page ref="pdf" @numPages="numPages=$event"></pdf>
    </div>
</template>

<script>
    import pdf from 'vue-pdf'
    export default {
        props: ['hide', 'httpServer', 'roomInfo'],
        components: {
            pdf: pdf
        },
        data: function () {
            return {
                page: 1,
                numpages: 0
            }
        },
        mounted() {
            this.httpServer.on('changePage', (obj) => {
                console.log('receive page:' + obj.page)
                this.page = obj.page
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
