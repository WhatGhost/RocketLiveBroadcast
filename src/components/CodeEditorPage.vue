<template>
    <div class="main-div" :class="{ hiding: hide }">
        <codemirror ref="codemirror" v-model="code" :options="editorOptions" @change="emitCodeChange" ></codemirror>
    </div>
</template>

<script>
import { CodeMirror, codemirror } from 'vue-codemirror'
export default {
    props: ['hide', 'httpServer', 'roomInfo', 'userInfo'],
    components: {
        CodeMirror,
        codemirror
    },
    created() {
        this.httpServer.on('changeCode', (obj) => {
            this.syncCode = obj.code
            this.code = obj.code
        })
        this.editorOptions['readOnly'] = !this.userInfo.isRoomCreator
    },
    data() {
        return {
            code: '',
            syncCode: '',
            editorOptions: {
                tabSize: 4,
                mode: 'text/javascript',
                theme: 'base16-light',
                lineNumbers: true,
                line: true,
                autofocus: true,
                readOnly: true
            }
        }
    },
    methods: {
        emitCodeChange(event) {
            if (event === this.syncCode) {
                return
            }
            this.httpServer.emit('changeCode', {
                roomId: this.roomInfo.roomId,
                code: event
            })
        }
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

/*.CodeMirror {*/
    /*text-align: left !important;*/
/*}*/
</style>
