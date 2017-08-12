<template>
    <div class="main-div" :class="{ hiding: hide }">
        <h1>PDFViewer</h1>
        <pdf src="../static/maplestory.pdf"></pdf>
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
            return {}
        },
    }
</script>

<style scoped>
    .hiding {
        display: none;
    }
</style>
