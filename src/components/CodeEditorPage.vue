<template>
    <div class="main-div" :class="{ hiding: hide }">
        <h1>Code Editor</h1>
        <vue-code v-model="code" :options="options" @ready="onReady"></vue-code>
    </div>
</template>

<script>
import VueCode from 'vue-code'
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/javascript/javascript'
export default {
    props: {
        'hide': true
    },
    components: {
        VueCode
    },
    data: function () {
        return {
            code: 'console.log("hello, world");',
            options: {
                mode: 'javascript',
            },
        }
    },
    methods: {
        onReady(cm) {
            console.log('Oh, you got the CodeMirror instance:', cm)
        },
    }
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
