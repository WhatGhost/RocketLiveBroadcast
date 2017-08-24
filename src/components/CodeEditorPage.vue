<template>
    <div class="main-div" :class="{ hiding: hide }">
        <label>
            <el-select ref="sel" class="codeLanguage" size="small"
                    v-model="editorOptions.mode">
                <el-option value="text/x-csrc" label="C">c</el-option>
                <el-option value="text/x-c++src" label="C++">c++</el-option>
                <el-option value="text/x-php" label="php">php</el-option>
                <el-option value="text/x-python" label="Python">python</el-option>
                <el-option value="text/html" label="HTML">html</el-option>
                <el-option value="text/x-java" label="Java">java</el-option>
                <el-option value="text/x-csharp" label="c#">c#</el-option>
                <el-option value="text/javascript" selected=true label="JavaScript">javascript</el-option>
                <el-option value="application/xml" label="XML">xml</el-option>
                <el-option value="text/css" label="CSS">css</el-option>
                <el-option value="text/x-go" label="go">go</el-option>
            </el-select>
        </label>
        <codemirror ref="codemirror" v-model="code" :options="editorOptions" @change="emitCodeChange" v-if="langChanged" ></codemirror>
    </div>
</template>

<script>
import { CodeMirror, codemirror } from 'vue-codemirror'
import 'codemirror/mode/clike/clike.js'
import 'codemirror/mode/python/python.js'
import 'codemirror/mode/javascript/javascript.js'
import 'codemirror/mode/htmlmixed/htmlmixed.js'
import 'codemirror/mode/css/css.js'
import 'codemirror/mode/vue/vue.js'
import 'codemirror/mode/php/php.js'
import 'codemirror/mode/go/go.js'

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
            this.editorOptions['mode'] = val
        }
    }
}
</script>
<style scoped>
.main-div {
    background-color: #f5f5f5;
}

.hiding {
    display: none;
}

</style>
