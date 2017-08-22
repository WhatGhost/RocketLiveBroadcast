<template>
    <div :class="{ hiding: hide }">
        <div class="fs-container">
            <div id="lc" ref="lcanvas"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['hide', 'httpServer', 'roomInfo', 'userInfo'],
    data: function () {
        return {
            lc: null,
            // drawing 用来在白板未加载出来时暂存画板数据
            drawing: null
        }
    },
    created() {
        this.httpServer.on('changeDrawing', (obj) => {
            if (this.lc === null) {
                this.drawing = obj.drawing
            } else {
                this.drawing = obj.drawing
                this.lc.loadSnapshot(JSON.parse(obj.drawing))
            }
        })
    },
    updated() {
        if (!this.lc) {
            this.mountlc()
            if (this.drawing !== null) {
                this.lc.loadSnapshot(JSON.parse(this.drawing))
            }
        }
    },
    methods: {
        mountlc: function () {
            this.lc = window.LC.init(document.getElementById('lc'), {
                imageURLPrefix: 'static/static/canvas/_assets/lc-images',
                toolbarPosition: 'bottom',
                defaultStrokeWidth: 2,
                strokeWidths: [1, 2, 3, 5, 30],
                imageSize: {
                    width: 580,
                    height: null
                }
            })
            if (this.userInfo.isRoomCreator) {
                this.lc.on('drawingChange', this.emitDrawingChange)
            }
        },
        emitDrawingChange: function () {
            this.httpServer.emit('changeDrawing', {
                roomId: this.roomInfo.roomId,
                drawing: JSON.stringify(this.lc.getSnapshot())
            })
        }
    }
}
</script>

<style scoped>
.hiding {
    display: none;
}

.fs-container {
    width: 580px;
    margin: auto;
}

.literally {
    width: 100%;
    height: 100%;
    position: relative;
}
</style>
