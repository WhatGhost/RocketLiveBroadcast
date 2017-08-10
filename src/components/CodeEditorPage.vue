<template>
    <div class="main-div" :class="{ hiding: hide }">
        <h1>Code Editor</h1>
    </div>
</template>

<script>
    export default {
        props: {
            'hide': true
        },
        data: function () {
            return {}
        },
//        methods: function () {
//        }
    }
</script>

<style scoped>
    .main-div {
        background-color: yellow;
    }

    .hiding {
        display: none;
    }
</style>
