<template>
    <div id="live-rooms" v-bind:class="{ blur: $store.state.background_blur }">
        <h1>直播房间</h1>
        <hr>
        <room v-for="room in rooms" v-bind:room="room"></room>
        <h1>录播记录</h1>
        <hr>
    </div>
</template>

<script>
import Room from './Room.vue'

export default {
    components: {
        Room
    },
    computed: {
        rooms() {
            return this.$store.state.rooms
        }
    }
}
</script>

<style scoped>
h1 {
    font-size: 20px;
    text-align: left;
    margin-left: 20px;
}
</style>
