<template>
    <div class="main-div" :class="{ hiding: hide }">
        <select ref="sel" class="codeLanguage" size="1" @change="update(selectLan.options[selectLan.options.selectedIndex].value)">
        <option value='text/x-csrc'>c</option>
        <option value='text/x-c++src'>c++</option>
        <option value='text/x-php'>php</option>
        <option value='text/x-python'>python</option>
        <option value='text/html'>html</option>
        <option value='text/x-java'>java</option>
        <option value='text/x-csharp'>c#</option>
        <option value='text/x-scala'>scala</option>
        <option value='text/javascript' selected=true>javascript</option>
        <option value='text/x-pascal'>pascal</option>
        <option value='text/x-ruby'>ruby</option>
        <option value='application/xml'>xml</option>
        <option value='text/css'>css</option>
        </select>    
        <button @click="changeC">change</button>
        <codemirror ref="codemirror" v-model="code" :options="editorOptions" @change="emitCodeChange" v-if="langChanged" ></codemirror>
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
            langChanged: true,
            code: '',
            syncCode: '',
            selectLan: null,
            editorOptions: {
                tabSize: 4,
                mode: 'text/x-python',
                theme: 'base16-light',
                lineNumbers: true,
                line: true,
                autofocus: true,
                readOnly: true
            }
        }
    },
    mounted: function() {
        this.selectLan = this.$refs.sel
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
        },
        update(val) {
            console.log(this.editorOptions['mode'])
            console.log('hhh')
            console.log(val)
            this.editorOptions['mode'] = val
        },
        changeC() {
            this.langChanged = !this.langChanged
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
