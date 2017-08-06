<!--<template>-->
    <!--<div id="roomlist">-->
        <!--<ul>-->
            <!--<room v-for="room in rooms" v-bind:room="room" v-bind:key="room.id">-->
            <!--</room>-->
        <!--</ul>-->
    <!--</div>-->
<!--</template>-->


<!--// <script>-->
<!--import Room from './Room.vue'-->

<!--export default {-->
    <!--components: {-->
        <!--Room-->
    <!--},-->
    <!--computed: {-->
        <!--rooms() {-->
            <!--return this.$store.state.rooms-->
        <!--}-->
    <!--}-->
<!--}-->
<!--</script>-->
<template>
    <div id="live-rooms">
        <h1>直播房间</h1>
        <room v-for="room in rooms" v-bind:room="room"></room>
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

</style>
