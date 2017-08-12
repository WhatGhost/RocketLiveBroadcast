<template>
    <div class="main-div" :class="{ hiding: hide }">
        <h1>PDFViewer</h1>
        <button @click="pgup">Previous Page</button>
        <button @click="pgdn">Next Page</button>
        <input v-model.number="page" type="number" style="width: 5em"> /{{numPages}}
        <pdf src="../static/maplestory.pdf" :page=page ref="pdf" @numPages="numPages=$event"></pdf>
    </div>
</template>

<script>
    import pdf from 'vue-pdf'
    export default {
        props: {
            hide: true,
        },
        components: {
            pdf: pdf
        },
        data: function () {
            return {
                page: 1,
                numpages: 0
            }
        },
        methods: {
            pgup() {
                this.page = this.page - 1
            },
            pgdn() {
                this.page = this.page + 1
            }
        }
    }
</script>

<style scoped>
    .hiding {
        display: none;
    }
</style>
