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
    /*display: flex;*/
    /*flex-direction: column;*/
    /*justify-content: center;*/
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
    width: 1200px;
    padding-left: 0;
}

@media screen and (max-width: 430px) { ul { width: 200px; } }
@media screen and (min-width: 431px) and (max-width: 630px) { ul { width: 400px; } }
@media screen and (min-width: 631px) and (max-width: 830px) { ul { width:600px;  } }
@media screen and (min-width: 831px) and (max-width: 1030px) { ul { width: 800px; } }
@media screen and (min-width: 1031px) and (max-width: 1230px) { ul { width: 1200px; } }
</style>
