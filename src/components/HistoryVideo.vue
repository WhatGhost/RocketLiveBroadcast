<template>
    <div class="main-div">
        <video class="video" v-bind:src="videoSource" controls="controls">
        </video>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            videoSource: ''
        }
    },
    methods: {
        getVideoSource: function () {
            for (let i = 0; i < this.$store.state.history.length; i++) {
                if (this.$store.state.history[i].room_id === parseInt(this.$route.params['id'])) {
                    let source = this.$store.state.history[i].history_source
                    this.videoSource = source
                    return
                }
            }
        }
    },
    beforeMount: function () {
        this.getVideoSource()
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
}

.video {
    width: 75%;
    margin: auto;
}
</style>
