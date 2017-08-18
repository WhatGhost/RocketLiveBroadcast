<template>
    <div :class="{ hiding: hide }">
        <button @click="mountlc">create</button>
        <div class="fs-container">
            <div id="lc" ref="lcanvas"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        hide: true,
    },
    // mounted() {
    //     this.lc = window.LC.init(document.getElementById('lc'), {
    //         imageURLPrefix: 'static/static/canvas/_assets/lc-images',
    //         toolbarPosition: 'bottom',
    //         defaultStrokeWidth: 2,
    //         strokeWidths: [1, 2, 3, 5, 30],
    //         imageSize: {
    //             width: 500,
    //             height: null
    //         }
    //     })
    // },
    data: function () {
        return {
            lc: null
        }
    },
    mounted() {
        this.lc = window.LC.init(this.$refs.lcanvas, {
            imageURLPrefix: 'static/static/canvas/_assets/lc-images',
            toolbarPosition: 'bottom',
            defaultStrokeWidth: 2,
            strokeWidths: [1, 2, 3, 5, 30],
            imageSize: {
                width: 500,
                height: null
            }
        })
    },
    methods: {
        out: function () {
            let j = JSON.stringify(this.lc.getSnapshot())
            console.log(j)
        },
        mountlc: function () {
            this.lc = window.LC.init(document.getElementById('lc'), {
                imageURLPrefix: 'static/static/canvas/_assets/lc-images',
                toolbarPosition: 'bottom',
                defaultStrokeWidth: 2,
                strokeWidths: [1, 2, 3, 5, 30],
                imageSize: {
                    width: 500,
                    height: null
                }
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
    width: 320px;
    margin: auto;
}

.literally {
    width: 100%;
    height: 100%;
    position: relative;
}
</style>
