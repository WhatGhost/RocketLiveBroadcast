<template>
    <div class="main-div" v-bind:class="{ blur: $store.state.background_blur }">
        <h1 class="live-title">Live Room</h1>
        <div class="live-rooms">
            <room class="room" v-for="room in rooms" v-show="room.active_mode === 'START'" v-bind:room="room" v-bind:key="count"></room>
        </div>
        <h1 class="history-title">History</h1>
        <div class="live-rooms">
            <room class="room" v-for="room in history" v-bind:room="room" v-bind:key="count"></room>
        </div>
    </div>
</template>

<script>
import Room from './Room.vue'

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
        rooms: function () {
            return this.$store.state.rooms
        },
        history: function () {
            return this.$store.state.history
        },
        count: function () {
            this.num += 1
            return this.num
        }
    },
    methods: {
        goHistory: function () {
            this.$router.push('/history')
        }
    }
}
</script>

<style scoped>
.main-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

h1 {
    font-size: 20px;
    text-align: center;
    margin-left: 20px;
    margin-top: 25px;
    color: white;
    padding: 20px;
    width: 140px;
}

.live-title {
    background-color: rgba(255, 211, 124, 0.5);
}

.history-title {
    background-color: rgba(125, 188, 169, 0.4);
}

.live-rooms {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    /*align-content: flex-start;*/
    /*align-content: space-around;*/
    width: 90%;
    margin-left: auto;
    margin-right: auto;
}

.room {
    width: 290px;
    overflow: hidden;
}
</style>
