<template>
    <div class="main-div" v-bind:class="{ blur: $store.state.background_blur }">
        <h1 class="live-title">Live Room</h1>
        <div class="live-rooms">
            <room class="room" v-for="room in rooms" v-show="room.active_mode === 'START'" v-bind:room="room" v-bind:key="count"></room>
        </div>
        <h1 class="history-title">History</h1>
    </div>
</template>

<script>
import Room from './Room.vue'
//    import Velocity from 'velocity-animate'

export default {
    components: {
        Room,
    },
    data: function () {
        return {
            num: 0
        }
    },
    computed: {
        rooms() {
            return this.$store.state.rooms
        },
        count() {
            this.num += 1
            return this.num
        }
    },
    methods: {}
}
</script>

<style scoped>
h1 {
    font-size: 20px;
    text-align: left;
    margin-left: 20px;
    margin-top: 25px;
    color: white;
    padding: 20px;
}

.live-title {
    background-color: rgba(29, 161, 242, 0.5);
}

.history-title {
    background-color: rgba(68, 41, 91, 0.4);
}

.live-rooms {
    display: flex;
    flex-wrap: wrap;
}

.room {
    width: 290px;
    overflow: hidden;
}
</style>
