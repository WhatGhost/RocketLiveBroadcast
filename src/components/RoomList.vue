<template>
    <div class="main-div" v-bind:class="{ blur: $store.state.background_blur }">
        <h1 class="live-title">Live Room</h1>
        <ul>
            <room v-for="(room, key) in rooms"
                  class="room"
                  v-show="room.active_mode === 'START'"
                  v-bind:room="room"
                  :isLive="true"
                  v-bind:key="key"></room>
        </ul>
        <h1 class="history-title">History</h1>
        <ul>
            <room v-for="(room, key) in history"
                  class="room"
                  v-bind:room="room"
                  :isLive="false"
                  v-bind:key="key"></room>
        </ul>
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

ul {
    margin: 0 auto;
    width: 1625px;
    padding-left: 0;
}

@media screen and (max-width: 400px) { ul { width: 320px; } }
@media screen and (min-width: 401px) and (max-width: 700px) { ul { width: 325px; } }
@media screen and (min-width: 701px) and (max-width: 1000px) { ul { width: 650px;  } }
@media screen and (min-width: 1001px) and (max-width: 1320px) { ul { width: 975px; } }
@media screen and (min-width: 1321px) and (max-width: 1650px) { ul { width: 1300px; } }
@media screen and (min-width: 1651px) and (max-width: 1950px) { ul { width: 1625px; } }
</style>
