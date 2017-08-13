<template>
    <div class="main-div" :class="{ hiding: hide }">
        <h1>Code Editor</h1>
        <codemirror v-model="code" :options="editorOptions"></codemirror>
    </div>
</template>

<script>
import { CodeMirror, codemirror } from 'vue-codemirror'
export default {
    props: {
        'hide': true
    },
    components: {
        CodeMirror,
        codemirror
    },
    data() {
        return {
            code: 'const a = 10',
            editorOptions: {
                // codemirror options
                tabSize: 4,
                mode: 'text/javascript',
                theme: 'base16-dark',
                lineNumbers: true,
                line: true
            }
        }
    },
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
