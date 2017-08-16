<template>
    <div class="main-div" v-bind:class="{ blur: $store.state.background_blur }">
        <h1 class="live-title">Live Room</h1>
        <!--<hr>-->
        <div class="live-rooms">
            <room class="room" v-for="room in rooms" v-bind:room="room" v-bind:key="count"></room>
        </div>
        <h1>History</h1>
        <!--<hr>-->
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
    background-color: rgba(0, 0, 0, 0.15);
    padding: 20px;
    /*margin-left: 0;*/
}

.live-rooms {
    display: flex;
    flex-wrap: wrap;
}

.room {
    width: 290px;
    overflow: hidden;
}

hr {
    display: block;
    height: 1px;
    border: 0;
    border-top: 1px solid #ccc;
    margin: 1em 0;
    padding: 0;
}
</style>
